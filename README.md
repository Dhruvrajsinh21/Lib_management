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

2. Change into the project directory:

```bash
cd Lib_management

3. Activate the virtual environment:

On windows:

```bash
venv\Scripts\activate

On Mac:

```bash
source venv\Scripts\activate

4. Install the required dependencies:

```bash
pip install -r requirements.txt

5. Change into the app directory:

```bash
cd app

6. Set up the database:

```bash
python create_db.py

7. Migrate the database:

```bash
flask db migrate
flask db upgrade

8. Run the Flask app:

```bash
python app.py

# API Endpoints:

## 1. User Authentication

POST api/auth/signup

Request body (payload):

```json
{
    "username": "your_username",
    "password": "your_password"
}

Response:
```json
{
    "message": "Signup successful"
}




