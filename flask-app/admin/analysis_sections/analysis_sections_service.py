from models import AnalysisSection 
from flask import render_template, abort, request, make_response, jsonify
from database import db



def find_all():
    analysis_sections = AnalysisSection.query.all()

    return render_template('analysis-sections.html',analysis_sections = analysis_sections)

def update_one(id):
  if request.method == 'GET':
    analysis_section = AnalysisSection.query\
        .filter_by(analysis_section_id = id)\
        .first()
  
    if not analysis_section:
      return abort(404)
    
    return render_template('update-analysis_section.html', analysis_section = analysis_section)

  data = request.form

  if not data.get('title'):
    return make_response("Formulaire invalide.", 400)

  analysis_section = AnalysisSection.query\
        .filter_by(analysis_section_id = id)\
        .first()

  if not analysis_section:
    return make_response("La section analyse n'existe pas.", 404)