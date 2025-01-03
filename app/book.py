from flask import request, jsonify
from models import db, Book
from flask_jwt_extended import jwt_required
from flask import Blueprint

# Add a new book (POST)
@jwt_required()
def add_book():
    data = request.get_json()
    if not data.get('title') or not data.get('author'):
        return jsonify({"message": "Title and author are required."}), 400

    new_book = Book(
        title=data['title'], 
        author=data['author'], 
        genre=data.get('genre', "Unknown")
    )
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify({"message": "Book added successfully", "book_id": new_book.id}), 201

# List all books (GET)
@jwt_required()
def list_books():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    books = Book.query.paginate(page=page, per_page=limit, error_out=False)
    
    results = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre} for book in books.items]
    
    return jsonify({
        "books": results, 
        "total": books.total, 
        "page": books.page, 
        "pages": books.pages,
        "limit": limit
    })

# Update book details (PUT)
@jwt_required() 
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get_or_404(book_id)

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)

    db.session.commit()
    
    return jsonify({"message": "Book updated successfully"}), 200

# Delete a book (DELETE)
@jwt_required() 
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    db.session.delete(book)
    db.session.commit()
    
    return jsonify({"message": "Book deleted successfully"}), 200
