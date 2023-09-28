from flask import Flask, render_template
from app_controller import main_router
from api import api_router
from admin import admin_router
import database as db
from flask_cors import CORS
import mail
import json
from crontab import crontab

def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '), ensure_ascii=False)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdxhfds iefhsdbf'
    CORS(app)

    app.register_blueprint(main_router)
    app.register_blueprint(admin_router, url_prefix= '/admin')
    app.register_blueprint(api_router, url_prefix = '/api')

    app.jinja_env.filters['tojson_pretty'] = to_pretty_json

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html")

    db.init(app)
    mail.init(app)
    crontab.init_app(app)
    #print crontab object as json

    return app
    
if __name__ == "__main__":
    create_app().run(host='localhost', port=3000, debug=True)