from models import AnalysisSubsection,AnalysisSection
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

def add_one(id):
  if request.method == 'POST':
      data = request.form

      last_analysis_subsection = AnalysisSubsection.query.order_by(AnalysisSubsection.analysis_section_id.desc(),AnalysisSubsection.analysis_subsection_id.desc()).first()
      if last_analysis_subsection:
        analysis_subsection_id = int(last_analysis_subsection.analysis_subsection_id) + 1
      else:
        analysis_subsection_id = 1
      while AnalysisSubsection.query.filter_by(analysis_subsection_id = analysis_subsection_id).first():
        analysis_subsection_id += 1

      analysis_subsection = AnalysisSubsection()
      analysis_subsection.analysis_subsection_id = analysis_subsection_id
      analysis_subsection.analysis_section_id = id
      analysis_subsection.title = data.get('title')
      analysis_subsection.description = data.get('description')
      analysis_subsection.order = data.get('order') #TODO what should be the default value for order?
      analysis_subsection.display_condition = data.get('display_condition') if data.get('display_condition') else None
      analysis_subsection.schema_type = data.get('schema_type') if data.get('schema_type') else None
      
      db.session.add(analysis_subsection)
      db.session.commit()
      return jsonify(analysis_subsection)

  return render_template('add-analysis-subsection.html', analysis_section_id = id)

def delete_one():
  analysis_subsection = AnalysisSubsection.query\
    .filter_by(analysis_subsection_id = id)\
    .first()

  if not analysis_subsection:
    return make_response("L'item n'existe pas.", 404)

  db.session.delete(analysis_subsection)
  db.session.commit()
  return jsonify(analysis_subsection)