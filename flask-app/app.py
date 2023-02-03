from flask import Flask
from os import path
from database import db
from user import User
from auth import auth_router 
from app_controller import main_router

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdxhfds iefhsdbf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    if not path.exists('admin-app/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')

    app.register_blueprint(auth_router, url_prefix='/auth')


    app.register_blueprint(main_router)

    return app
    

if __name__ == "__main__":
    create_app().run(debug=True)
