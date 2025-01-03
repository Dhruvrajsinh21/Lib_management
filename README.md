# Library Management System

This is a Flask-based application for managing books, members, and users with JWT authentication. The app allows users to sign up, log in, add books, and manage members, all with secure JWT token-based authentication.

# Features:

- **User Authentication**: Users can log in and receive a JWT token for authentication.
- **Book Management**: User can add, update, list, and delete books.
- **Member Management**: User can register, update, delete, and list members.
- **JWT Authentication**: All routes related to book management and member management require JWT authentication.

# Required Python libraries:

1. Flask
2. Flask-SQLAlchemy
3. Flask-JWT-Extended
5. SQLite (default database)

# Installation:

1. Clone the repository:

```bash
git clone https://github.com/Dhruvrajsinh21/Lib_management
```

2. Change into the project directory:

```bash
cd Lib_management
```

3. Activate the virtual environment:

```bash
venv\Scripts\activate #Window
```

```bash
source venv\Scripts\activate #Mac
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Change into the app directory:

```bash
cd app
```

6. Set up the database:

```bash
python create_db.py
#This will create the SQLite database (library.db) with the necessary tables as defined in the models.py file.
```

7. Migrate the database:

```bash
flask db migrate
flask db upgrade
```

8. Run the Flask app:

```bash
python app.py
```
Open your browser and Postman and visit http://localhost:5000/ to start using the application.

# API Endpoints:

## 1. User Authentication

POST api/auth/signup

Request body (payload):

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response:

```json
{
    "message": "Signup successful"
}
```

POST api/auth/login: Logs in a user and returns a JWT token.

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response:

```json
{
    "access_token": "your_jwt_token"
}
```

## 2. Book Management:

POST /books: Adds a new book. Requires JWT authentication.
```http
POST /books/
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

Payload:

```json
{
  "title": "Book Title",
  "author": "Author Name",
  "genre": "Genre (optional)"
}
```
Response:
```json
{
  "message": "Book added successfully",
  "book_id": 1
}
```
List All Books (GET):

```http
GET /books/
Authorization: Bearer <JWT_TOKEN>
```
Query Parameters:

page (optional): Page number (default: 1)
limit (optional): Number of items per page (default: 10)

Response:

```json
{
  "books": [
    {"id": 1, "title": "Book Title", "author": "Author Name", "genre": "Genre"}
  ],
  "total": 1,
  "page": 1,
  "pages": 1,
  "limit": 10
}
```
Update a Book (PUT):

```http
PUT /books/<book_id>
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

Request Body:

``json
{
  "title": "Updated Title",
  "author": "Updated Author",
  "genre": "Updated Genre"
}
```
Response:

```json
{
  "message": "Book updated successfully"
}
```




