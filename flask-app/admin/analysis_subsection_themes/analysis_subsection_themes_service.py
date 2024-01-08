from models import AnalysisSubsection,AnalysisSection, AnalysisSubsectionTheme, AnalysisSubsectionSubtheme
from flask import render_template, abort, request, make_response, jsonify
from database import db

def find_one(id):
  analysis_subsection_theme = AnalysisSubsectionTheme.query\
    .filter_by(analysis_subsection_theme_id = id)\
    .first()
  
  if not analysis_subsection_theme:
    return abort(404)
  
  analysis_subsection_subthemes = AnalysisSubsectionSubtheme.query\
    .filter_by(analysis_subsection_theme_id = id)\
    .all()
  
  return render_template('analysis-subsection-theme.html', analysis_subsection_theme = analysis_subsection_theme, analysis_subsection_subthemes = analysis_subsection_subthemes)

def update_one(id):
  if request.method == 'GET':
    theme = AnalysisSubsectionTheme.query\
        .filter_by(analysis_subsection_theme_id = id)\
        .first()
  
    if not theme:
      return abort(404)
    
    return render_template('update-analysis-subsection-theme.html', analysis_subsection_theme = theme)

  data = request.form

  if not data.get('title'):
    return "Formulaire invalide.", 400

  theme = AnalysisSubsectionTheme.query\
        .filter_by(analysis_subsection_theme_id = id)\
        .first()

  if not theme:
    return "Le thème n'existe pas.", 404
  
  theme.name = data.get('title')
  theme.is_active = 1 if data.get('is_active') else 0
  db.session.commit()
  return jsonify(theme)

def add_one(id):
  if request.method == 'POST':
      data = request.form

      last_theme = AnalysisSubsectionTheme.query.order_by(AnalysisSubsectionTheme.analysis_subsection_theme_id.desc()).first()
      if last_theme:
        analysis_subsection_theme_id = int(last_theme.analysis_subsection_theme_id) + 1
      else:
        analysis_subsection_theme_id = 1
      while AnalysisSubsectionTheme.query.filter_by(analysis_subsection_theme_id = analysis_subsection_theme_id).first():
        analysis_subsection_theme_id += 1

      theme = AnalysisSubsectionTheme()
      theme.analysis_subsection_theme_id = analysis_subsection_theme_id
      theme.analysis_subsection_id = id 
      theme.name = data.get('title')
      theme.is_active = 1 if data.get('is_active') else 0
      
      db.session.add(theme)
      db.session.commit()
      return jsonify(theme)

  return render_template('add-analysis-subsection-theme.html', analysis_subsection_id = id)

def delete_one(id):
  item = AnalysisSubsectionTheme.query\
    .filter_by(analysis_subsection_theme_id = id)\
    .first()

  if not item:
    return make_response("L'item n'existe pas.", 404)

  db.session.delete(item)
  db.session.commit()
  return jsonify(item)