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

  if not data.get('title') or not data.get('description') or not data.get('order'):
    return "Formulaire invalide.", 400

  analysis_subsection = AnalysisSubsection.query\
        .filter_by(analysis_subsection_id = id)\
        .first()

  if not analysis_subsection:
    return "La section d'analyse n'existe pas.", 404

  analysis_subsection.title = data.get('title')
  analysis_subsection.description = data.get('description')
  analysis_subsection.order = data.get('order') #TODO what should be the default value for order?
  analysis_subsection.display_condition = data.get('display_condition') if data.get('display_condition') else None
  analysis_subsection.schema_type = data.get('schema_type') if data.get('schema_type') else None
  db.session.commit()
  return jsonify(analysis_subsection)