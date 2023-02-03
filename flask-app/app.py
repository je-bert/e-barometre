from flask import Flask
from os import path
from database import db

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdxhfds iefhsdbf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from user_model import User

    if not path.exists('admin-app/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')

    from auth_controller import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app_controller import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
    

if __name__ == "__main__":
    create_app().run(debug=True)
