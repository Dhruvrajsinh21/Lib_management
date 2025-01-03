from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Member

# Register a new member (POST)
@jwt_required()
def register_member():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not all([name, email]):
        return jsonify({"message": "Name, email are required"}), 400

    if Member.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 400
    
    new_member = Member(name=name, email=email)
    db.session.add(new_member)
    db.session.commit()

    return jsonify({"message": "Member registered successfully"}), 201

# List all members (GET)
@jwt_required()
def list_members():

    current_user = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    members = Member.query.paginate(page=page, per_page=limit, error_out=False)
    results = [{"id": member.id, "name": member.name, "email": member.email} for member in members.items]
    return jsonify({
        "members": results, 
        "total": members.total, 
        "page": members.page, 
        "pages": members.pages,
        "limit": limit
    }), 200

# Update member details (PUT)
@jwt_required()
def update_member(member_id):

    current_user = get_jwt_identity()
    data = request.get_json()
    member = Member.query.get_or_404(member_id)
    member.name = data.get('name', member.name)
    member.email = data.get('email', member.email)
    db.session.commit()

    return jsonify({"message": "Member updated successfully"}), 200

# Delete a member (DELETE)
@jwt_required()
def delete_member(member_id):

    current_user = get_jwt_identity()
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()

    return jsonify({"message": "Member deleted successfully"}), 200
