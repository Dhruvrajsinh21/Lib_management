from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models import db, User
from werkzeug.security import check_password_hash

# Signup function for members (POST)
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Email already exists"}), 400

    new_member = User(username=username)
    new_member.set_password(password)
    db.session.add(new_member)
    db.session.commit()

    return jsonify({"message": "Signup successful"}), 201

# Login function for users (POST)
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    identity = str(user.id)
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token}), 200
