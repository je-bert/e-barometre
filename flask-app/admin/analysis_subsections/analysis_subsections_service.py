from models import AnalysisSubsection,AnalysisSection, AnalysisSubsectionItem, AnalysisSubsectionTheme, AnalysisSubsectionSubtheme
from flask import render_template, abort, request, make_response, jsonify
from database import db
from sqlalchemy import func

def find_one(id):
  analysis_subsection = AnalysisSubsection.query\
    .filter_by(analysis_subsection_id = id)\
    .first()
  
  if not analysis_subsection:
    return abort(404)
  
  analysis_subsection_items = AnalysisSubsectionItem.query\
    .filter_by(analysis_subsection_id = id)\
    .all()
  
  analysis_subsection_themes = AnalysisSubsectionTheme.query\
    .filter_by(analysis_subsection_id = id)\
    .all()
  
  analysis_subsection_themes = db.session.query(
      AnalysisSubsectionTheme.analysis_subsection_theme_id, 
      AnalysisSubsectionTheme.analysis_subsection_id, 
      AnalysisSubsectionTheme.is_active, 
      AnalysisSubsectionTheme.name, 
      func.count(AnalysisSubsectionSubtheme.analysis_subsection_subtheme_id).label("subthemes_count")
      )\
      .select_from(AnalysisSubsectionTheme).filter_by(analysis_subsection_id = id).outerjoin(AnalysisSubsectionSubtheme)\
      .group_by(AnalysisSubsectionTheme.analysis_subsection_theme_id)\
      .all()

  return render_template('analysis-subsection.html',analysis_subsection = analysis_subsection, analysis_subsection_items = analysis_subsection_items, analysis_subsection_themes = analysis_subsection_themes)

def update_one(id):
  if request.method == 'GET':
    analysis_subsection = AnalysisSubsection.query\
        .filter_by(analysis_subsection_id = id)\
        .first()
  
    if not analysis_subsection:
      return abort(404)
    
    return render_template('update-analysis-subsection.html', analysis_subsection = analysis_subsection)

  data = request.form

  if not data.get('title') or not data.get('about_barometer') or not data.get('order') or not data.get('schema_type'):
    return "Formulaire invalide.", 400

  analysis_subsection = AnalysisSubsection.query\
        .filter_by(analysis_subsection_id = id)\
        .first()

  if not analysis_subsection:
    return "La section d'analyse n'existe pas.", 404

  analysis_subsection.title = data.get('title')
  analysis_subsection.about_barometer = data.get('about_barometer')
  analysis_subsection.order = data.get('order')
  analysis_subsection.min_result = float(data.get('min_result')) if data.get('min_result') else 0
  analysis_subsection.min_weight = float(data.get('min_weight')) if data.get('min_weight') else 0
  analysis_subsection.schema_type = data.get('schema_type') if data.get('schema_type') else None
  analysis_subsection.is_active = 1 if data.get('is_active') else 0
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
      analysis_subsection.about_barometer = data.get('about_barometer')
      analysis_subsection.order = data.get('order') #TODO what should be the default value for order?
      analysis_subsection.barometer = data.get('schema_type') if data.get('schema_type') else None
      analysis_subsection.is_active = 1 if data.get('is_active') else 0
      analysis_subsection.min_result = float(data.get('min_result')) if data.get('min_result') else 0
      analysis_subsection.min_weight = float(data.get('min_weight')) if data.get('min_weight') else 0
      
      db.session.add(analysis_subsection)
      db.session.commit()
      return jsonify(analysis_subsection)

  return render_template('add-analysis-subsection.html', analysis_section_id = id)

def delete_one(id):
  analysis_subsection = AnalysisSubsection.query\
    .filter_by(analysis_subsection_id = id)\
    .first()

  if not analysis_subsection:
    return make_response("L'item n'existe pas.", 404)

  db.session.delete(analysis_subsection)
  db.session.commit()
  return jsonify(analysis_subsection)