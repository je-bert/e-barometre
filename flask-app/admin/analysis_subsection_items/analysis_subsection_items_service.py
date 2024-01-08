from models import AnalysisSection, AnalysisSubsection, AnalysisSubsectionItem,AnalysisSubsectionTheme, AnalysisSubsectionSubtheme 
from flask import render_template, abort, request, make_response, jsonify
from database import db
import json

def update_one(id):
  if request.method == 'GET':
    analysis_subsection_item = AnalysisSubsectionItem.query\
        .filter_by(analysis_subsection_item_id = id)\
        .first()
  
    if not analysis_subsection_item:
      return abort(404)
    
    analysis_subsection_themes = AnalysisSubsectionTheme.query\
      .filter_by(analysis_subsection_id = analysis_subsection_item.analysis_subsection_id)\
      .all()
    
    analysis_subsection_subthemes = []
    for theme in analysis_subsection_themes:
      analysis_subsection_subthemes += AnalysisSubsectionSubtheme.query\
        .filter_by(analysis_subsection_theme_id = theme.analysis_subsection_theme_id)\
        .all()
      
    link_to_choices = [{'id': None, 'name': 'Baromètre', 'type': 'none'}]
    current_link_to = link_to_choices[0]

    for theme in analysis_subsection_themes:
      link_to_choices.append({
        'id': theme.analysis_subsection_theme_id,
        'name': "Thème " + (theme.name if theme.name else 'sans nom'),
        'type': 'theme'
      })
      if int(theme.analysis_subsection_theme_id) == analysis_subsection_item.analysis_subsection_theme_id:
        current_link_to = link_to_choices[-1]
    for subtheme in analysis_subsection_subthemes:
      link_to_choices.append({
        'id': subtheme.analysis_subsection_subtheme_id,
        'name': "Comportement " + subtheme.question_id,
        'type': 'subtheme'
      })
      if int(subtheme.analysis_subsection_subtheme_id) == analysis_subsection_item.analysis_subsection_subtheme_id:
        current_link_to = link_to_choices[-1]
    
    return render_template('update-analysis-subsection-item.html', analysis_subsection_item = analysis_subsection_item, link_to_choices = link_to_choices, current_link_to = current_link_to)

  data = request.form

  if not data.get('content') or not data.get('min') or not data.get('max') or not data.get('type') or not data.get('link_to_choice'):
    return "Formulaire invalide.", 400

  analysis_subsection_item = AnalysisSubsectionItem.query\
      .filter_by(analysis_subsection_item_id = id)\
      .first()

  if not analysis_subsection_item:
    return "L'item n'existe pas.", 404
  
  analysis_subsection_item.content = data.get('content')
  link_to_choice = data.get('link_to_choice').split(",")
  if (link_to_choice[0] == 'theme'):
    analysis_subsection_item.analysis_subsection_theme_id = link_to_choice[1]
    analysis_subsection_item.analysis_subsection_subtheme_id = None
  elif (link_to_choice[0] == 'subtheme'):
    analysis_subsection_item.analysis_subsection_theme_id = None
    analysis_subsection_item.analysis_subsection_subtheme_id = link_to_choice[1]
  else:
    analysis_subsection_item.analysis_subsection_theme_id = None
    analysis_subsection_item.analysis_subsection_subtheme_id = None
  analysis_subsection_item.min = float(data.get('min'))
  analysis_subsection_item.max = float(data.get('max'))
  analysis_subsection_item.type = data.get('type')
  analysis_subsection_item.is_active = 1 if data.get('is_active') else 0
  db.session.commit()
  
  return jsonify(analysis_subsection_item)

def add_one(id):
  if request.method == 'POST':
      data = request.form

      if not data.get('content') or not data.get('min') or not data.get('max') or not data.get('type') or not data.get('link_to_choice'):
        return make_response("Formulaire invalide.", 400)
      
      last_item = AnalysisSubsectionItem.query.order_by(AnalysisSubsectionItem.analysis_subsection_item_id.desc()).first()
      if last_item:
        analysis_subsection_item_id = int(last_item.analysis_subsection_item_id) + 1
      else:
        analysis_subsection_item_id = 1
      while AnalysisSubsectionItem.query.filter_by(analysis_subsection_item_id = analysis_subsection_item_id).first():
        analysis_subsection_item_id += 1
       
      analysis_subsection_item = AnalysisSubsectionItem()
      analysis_subsection_item.analysis_subsection_item_id = analysis_subsection_item_id
      analysis_subsection_item.analysis_subsection_id =  id
      analysis_subsection_item.content = data.get('content')
      link_to_choice = data.get('link_to_choice').split(",")
      if (link_to_choice[0] == 'theme'):
        analysis_subsection_item.analysis_subsection_theme_id = link_to_choice[1]
        analysis_subsection_item.analysis_subsection_subtheme_id = None
      elif (link_to_choice[0] == 'subtheme'):
        analysis_subsection_item.analysis_subsection_theme_id = None
        analysis_subsection_item.analysis_subsection_subtheme_id = link_to_choice[1]
      else:
        analysis_subsection_item.analysis_subsection_theme_id = None
        analysis_subsection_item.analysis_subsection_subtheme_id = None
      analysis_subsection_item.min = float(data.get('min'))
      analysis_subsection_item.max = float(data.get('max'))
      analysis_subsection_item.type = data.get('type')
      analysis_subsection_item.is_active = 1 if data.get('is_active') else 0
      db.session.add(analysis_subsection_item)
      db.session.commit()

      return jsonify(analysis_subsection_item)
  else:
    analysis_subsection_themes = AnalysisSubsectionTheme.query\
        .filter_by(analysis_subsection_id = id)\
        .all()
      
    analysis_subsection_subthemes = []
    for theme in analysis_subsection_themes:
        analysis_subsection_subthemes += AnalysisSubsectionSubtheme.query\
          .filter_by(analysis_subsection_theme_id = id)\
          .all()
        
    link_to_choices = [{'id': None, 'name': 'Baromètre', 'type': 'none'}]

    for theme in analysis_subsection_themes:
      link_to_choices.append({
        'id': theme.analysis_subsection_theme_id,
        'name': "Thème " + (theme.name if theme.name else 'sans nom'),
        'type': 'theme'
      })
    for subtheme in analysis_subsection_subthemes:
      link_to_choices.append({
        'id': subtheme.analysis_subsection_subtheme_id,
        'name': "Comportement " + subtheme.question_id,
        'type': 'subtheme'
      })

    return render_template('add-analysis-subsection-item.html', analysis_subsection_id = id, link_to_choices = link_to_choices)

def delete_one(id):
    item = AnalysisSubsectionItem.query\
        .filter_by(analysis_subsection_item_id = id)\
        .first()
    
    if not item:
      return make_response("L'item n'existe pas.", 404)
    
    db.session.delete(item)
    db.session.commit()
    return 'Item supprimé'