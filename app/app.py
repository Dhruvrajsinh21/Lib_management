from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db
from routes import library_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'
    
    db.init_app(app)
    JWTManager(app)
    migrate = Migrate(app, db)

    app.register_blueprint(library_bp)

    # This is only for when you want to automatically create the tables during the app initialization
    # with app.app_context():
    #     db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
