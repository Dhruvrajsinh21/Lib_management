from flask import Blueprint
from authentication import signup, login
from book import *
from member import *
# Create a Blueprint for the library
library_bp = Blueprint('library', __name__)

# -------- Authentication APIs --------
library_bp.add_url_rule('/api/auth/signup', view_func=signup, methods=['POST'])
library_bp.add_url_rule('/api/auth/login', view_func=login, methods=['POST'])

# -------- Book APIs --------
library_bp.add_url_rule('/api/books', view_func=add_book, methods=['POST'])
library_bp.add_url_rule('/api/books', view_func=list_books, methods=['GET'])
library_bp.add_url_rule('/api/books/<int:book_id>', view_func=update_book, methods=['PUT'])
library_bp.add_url_rule('/api/books/<int:book_id>', view_func=delete_book, methods=['DELETE'])

# -------- Member APIs --------
library_bp.add_url_rule('/api/members', view_func=register_member, methods=['POST'])
library_bp.add_url_rule('/api/members', view_func=list_members, methods=['GET'])
library_bp.add_url_rule('/api/members/<int:member_id>', view_func=update_member, methods=['PUT'])
library_bp.add_url_rule('/api/members/<int:member_id>', view_func=delete_member, methods=['DELETE'])
