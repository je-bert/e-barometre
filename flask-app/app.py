from flask import Flask, render_template
from auth import auth_router 
from app_controller import main_router
from surveys import surveys_router
from questions import questions_router
from labels import labels_router
from db import db_router
import database as db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdxhfds iefhsdbf'

    app.register_blueprint(auth_router, url_prefix='/auth')
    app.register_blueprint(main_router)
    app.register_blueprint(surveys_router, url_prefix='/surveys')
    app.register_blueprint(questions_router, url_prefix='/questions')
    app.register_blueprint(labels_router, url_prefix='/labels')
    app.register_blueprint(db_router, url_prefix='/db')

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html")

    db.init(app)

    return app
    
if __name__ == "__main__":
    create_app().run(debug=True)
