from flask import Blueprint, render_template, redirect, url_for

main_router = Blueprint('main_router', __name__)

@main_router.route('/')
def index():
    return redirect(url_for("admin_router.surveys_router.find_all"))