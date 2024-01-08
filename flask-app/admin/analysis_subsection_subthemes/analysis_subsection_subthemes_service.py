from models import AnalysisSubsection,AnalysisSection, AnalysisSubsectionSubtheme, Question
from flask import render_template, abort, request, make_response, jsonify
from database import db

def update_one(id):
  if request.method == 'GET':
    subtheme = AnalysisSubsectionSubtheme.query\
        .filter_by(analysis_subsection_subtheme_id = id)\
        .first()
  
    if not subtheme:
      return abort(404)

    questions = Question.query\
      .all()
    
    return render_template('update-analysis-subsection-subtheme.html', analysis_subsection_subtheme = subtheme, questions=questions)

  data = request.form

  if not data.get('question_id') or not data.get('ranges'):
    return "Formulaire invalide.", 400

  subtheme = AnalysisSubsectionSubtheme.query\
        .filter_by(analysis_subsection_subtheme_id = id)\
        .first()

  if not subtheme:
    return "Le sous-thème n'existe pas.", 404
  
  subtheme.question_id = data.get('question_id')
  subtheme.ranges = data.get('ranges')
  subtheme.is_active = 1 if data.get('is_active') else 0
  subtheme.weight = data.get('weight') if data.get('weight') else 0
  subtheme.itensity = data.get('itensity') if data.get('itensity') else 0
  db.session.commit()
  return jsonify(subtheme)

def add_one(id):
  if request.method == 'POST':
      data = request.form

      last_subtheme = AnalysisSubsectionSubtheme.query.order_by(AnalysisSubsectionSubtheme.analysis_subsection_subtheme_id.desc()).first()
      if last_subtheme:
        analysis_subsection_subtheme_id = int(last_subtheme.analysis_subsection_subtheme_id) + 1
      else:
        analysis_subsection_subtheme_id = 1
      while AnalysisSubsectionSubtheme.query.filter_by(analysis_subsection_subtheme_id = analysis_subsection_subtheme_id).first():
        analysis_subsection_subtheme_id += 1

      subtheme = AnalysisSubsectionSubtheme()
      subtheme.analysis_subsection_subtheme_id = analysis_subsection_subtheme_id
      subtheme.analysis_subsection_theme_id = id
      subtheme.question_id = data.get('question_id')
      subtheme.ranges = data.get('ranges')
      subtheme.is_active = 1 if data.get('is_active') else 0
      subtheme.weight = data.get('weight') if data.get('weight') else 0
      subtheme.intensity = data.get('intensity') if data.get('intensity') else 0
      db.session.add(subtheme)
      db.session.commit()
      return jsonify(subtheme)

  questions = Question.query\
    .all()

  return render_template('add-analysis-subsection-subtheme.html', analysis_subsection_theme_id = id, questions = questions)

def delete_one(id):
  item = AnalysisSubsectionSubtheme.query\
    .filter_by(analysis_subsection_subtheme_id = id)\
    .first()

  if not item:
    return make_response("L'item n'existe pas.", 404)

  db.session.delete(item)
  db.session.commit()
  return jsonify(item)