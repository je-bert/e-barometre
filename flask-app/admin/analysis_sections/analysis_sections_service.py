from models import AnalysisSection, AnalysisSubsection, AnalysisSubsectionItem, AnalysisSubsectionTheme, AnalysisSubsectionSubtheme
from flask import render_template, abort, request, make_response, jsonify
from database import db
from sqlalchemy import func



def find_all():
    analysis_sections = db.session.query(
      AnalysisSection.analysis_section_id, 
      AnalysisSection.is_active, 
      AnalysisSection.order, 
      AnalysisSection.title, 
      func.count(AnalysisSubsection.analysis_subsection_id).label("subsections_count")
      )\
      .select_from(AnalysisSection).outerjoin(AnalysisSubsection)\
      .group_by(AnalysisSection.analysis_section_id)\
      .all()
    return render_template('analysis-sections.html', analysis_sections = analysis_sections)


def find_one(id):
  analysis_section = AnalysisSection.query\
    .filter_by(analysis_section_id = id)\
    .first()
  
  if not analysis_section:
    return abort(404)
  
  analysis_subsections = db.session.query(
      AnalysisSubsection.analysis_section_id, 
      AnalysisSubsection.analysis_subsection_id, 
      AnalysisSubsection.is_active, 
      AnalysisSubsection.order, 
      AnalysisSubsection.title, 
      AnalysisSubsection.about_barometer, 
      AnalysisSubsection.barometer, 
      AnalysisSubsection.min_result,
      AnalysisSubsection.min_weight,
      func.count(AnalysisSubsectionTheme.analysis_subsection_theme_id).label("themes_count")
      )\
      .select_from(AnalysisSubsection).filter_by(analysis_section_id = id).outerjoin(AnalysisSubsectionTheme)\
      .group_by(AnalysisSubsection.analysis_subsection_id)\
      .all()

  return render_template('analysis-subsections.html',analysis_section = analysis_section, analysis_subsections = analysis_subsections)

def update_one(id):
  if request.method == 'GET':
    analysis_section = AnalysisSection.query\
        .filter_by(analysis_section_id = id)\
        .first()
  
    if not analysis_section:
      return abort(404)
    
    return render_template('update-analysis-section.html', analysis_section = analysis_section)

  data = request.form

  if not data.get('title') or not data.get('order'):
    return "Formulaire invalide.", 400

  analysis_section = AnalysisSection.query\
    .filter_by(analysis_section_id = id)\
    .first()

  if not analysis_section:
    return "La section d'analyse n'existe pas.", 404

  analysis_section.title = data.get('title')
  analysis_section.order = data.get('order')
  analysis_section.is_active = 1 if data.get('is_active') else 0
  db.session.commit()
  
  return jsonify(analysis_section)

def add_one():
  if request.method == 'POST':
      data = request.form

      if not data.get('title'):
          return make_response("Formulaire invalide.", 400)
      
      last_analysis_section = AnalysisSection.query.order_by(AnalysisSection.analysis_section_id.desc(),AnalysisSection.analysis_section_id.desc()).first()
      if last_analysis_section:
        analysis_section_id = int(last_analysis_section.analysis_section_id) + 1
      else:
        analysis_section_id = 1
      while AnalysisSection.query.filter_by(analysis_section_id = analysis_section_id).first():
        analysis_section_id += 1
       
      analysis_section = AnalysisSection()
      analysis_section.analysis_section_id = analysis_section_id
      analysis_section.title = data.get('title')
      analysis_section.order = data.get('order')
      analysis_section.is_active = 1 if data.get('is_active') else 0
      db.session.add(analysis_section)
      db.session.commit()

      return jsonify(analysis_section)

  return render_template('add-analysis-section.html')

def delete_one(id):
    analysis_section = AnalysisSection.query\
        .filter_by(analysis_section_id = id)\
        .first()
    
    if not analysis_section:
      return make_response("L'item n'existe pas.", 404)
    
    db.session.delete(analysis_section)
    db.session.commit()
    return 'Section d\'analyse supprimée'