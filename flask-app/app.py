from flask import Flask
from os import path
from auth import auth_router 
from app_controller import main_router
import database as db
from sys import argv

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdxhfds iefhsdbf'

    db.init_app(app)

    app.register_blueprint(auth_router, url_prefix='/auth')

    app.register_blueprint(main_router)

    return app
    

if __name__ == "__main__":
    create_app().run(debug=True)
