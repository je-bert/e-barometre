from flask import Blueprint, render_template
from admin.surveys import surveys_router
from admin.questions import questions_router
from admin.labels import labels_router
from admin.label_items import label_items_router
from admin.db import db_router
from admin.report_template import report_template_router
from admin.auth import auth_router
from admin.results import results_router
from admin.analysis import analysis_router


admin_router = Blueprint('admin_router', __name__)

admin_router.register_blueprint(surveys_router, url_prefix='/surveys')
admin_router.register_blueprint(questions_router, url_prefix='/questions')
admin_router.register_blueprint(labels_router, url_prefix='/labels')
admin_router.register_blueprint(label_items_router, url_prefix='/label-items')
admin_router.register_blueprint(db_router, url_prefix='/db')
admin_router.register_blueprint(auth_router, url_prefix='/auth')
admin_router.register_blueprint(results_router, url_prefix='/results')
admin_router.register_blueprint(analysis_router,url_prefix='/analysis')
admin_router.register_blueprint(report_template_router,url_prefix='/report-template')


@admin_router.route('/glossary')
def glossary():
    return render_template("glossary.html")