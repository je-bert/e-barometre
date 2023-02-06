from flask import Blueprint, render_template, redirect, url_for
from auth import auth

main_router = Blueprint('main_router', __name__)

@main_router.route('/')
@auth
def index():
    return redirect(url_for("surveys_router.find_all"))

@main_router.route('/glossary')
@auth
def glossary():
    return render_template("glossary.html")