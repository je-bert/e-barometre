from models import AnalysisSubsection
from flask import render_template, abort, request, make_response, jsonify
from database import db

def update_one(id):
  if request.method == 'GET':
    analysis_subsection = AnalysisSubsection.query\
        .filter_by(analysis_subsection_id = id)\
        .first()
  
    if not analysis_subsection:
      return abort(404)
    
    return render_template('update-analysis-subsection.html', analysis_subsection = analysis_subsection)

  data = request.form

# TODO title should be mandatory right?
  if not data.get('title'):
    return make_response("Formulaire invalide.", 400)

  analysis_subsection = AnalysisSubsection.query\
        .filter_by(analysis_section_id = id)\
        .first()

  if not analysis_subsection:
    return make_response("La section d'analyse n'existe pas.", 404)

# TODO check the required fields 
  analysis_subsection.title = data.get('title')
  analysis_subsection.description = data.get('description') if data.get('description') else None
  analysis_subsection.order = data.get('order') #TODO what should be the default value for order?
  analysis_subsection.display_condition = data.get('display_condition') if data.get('display_condition') else None
  analysis_subsection.schema_type = data.get('schema_type') if data.get('schema_type') else None
  db.session.commit()
  return jsonify(analysis_subsection)