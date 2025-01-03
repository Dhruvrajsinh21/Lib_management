from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash  # For password hashing

# Initialize the database
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        """Hash the password before storing it"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check if the password matches the hash"""
        return check_password_hash(self.password, password)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=True, default="Unknown")

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

    def update(self, title=None, author=None, genre=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        db.session.commit()

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Member {self.name}, {self.email}>"

