from models import AnalysisSection, AnalysisSubsection
from flask import render_template, abort, request, make_response, jsonify
from database import db



def find_all():
    analysis_sections = AnalysisSection.query.all()

    return render_template('analysis-sections.html',analysis_sections = analysis_sections)


def find_one(id):
  analysis_section = AnalysisSection.query\
                      .filter_by(analysis_section_id = id)\
                      .first()
  if not analysis_section:
    return abort(404)
  
  # to return all the analysis subsections related to the section TODO remove comment after
  analysis_subsections = AnalysisSubsection.query\
                        .filter_by(analysis_section_id = id)\
                        .all()

  if not analysis_subsections:
    return abort(404)

  return render_template('analysis-subsections.html',analysis_section = analysis_section,analysis_subsections = analysis_subsections)

def update_one(id):
  if request.method == 'GET':
    analysis_section = AnalysisSection.query\
        .filter_by(analysis_section_id = id)\
        .first()
  
    if not analysis_section:
      return abort(404)
    
    return render_template('update-analysis-section.html', analysis_section = analysis_section)

  data = request.form

# TODO title should be mandatory right?
  if not data.get('title'):
    return make_response("Formulaire invalide.", 400)

  analysis_section = AnalysisSection.query\
        .filter_by(analysis_section_id = id)\
        .first()

  if not analysis_section:
    return make_response("La section d'analyse n'existe pas.", 404)

# TODO check the required fields 
  analysis_section.title = data.get('title')
  analysis_section.description = data.get('description') if data.get('description') else None
  analysis_section.order = data.get('order') #TODO what should be the default value for order?
  db.session.commit()
  return jsonify(analysis_section)