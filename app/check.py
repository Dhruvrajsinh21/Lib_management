from app import create_app, db
from sqlalchemy import inspect

# Initialize the app
app = create_app()

with app.app_context():
    # Use SQLAlchemy's inspect method to check if the tables exist
    inspector = inspect(db.engine)
    
    book_table_exists = inspector.has_table('books')
    #member_table_exists = inspector.has_table('members')
    member_table_exists = inspector.has_table('Users')
    
    # Output the results
    if book_table_exists and member_table_exists:
        print("Tables are created successfully!")
    else:
        print("Tables are not created!")
