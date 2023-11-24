from models import Question, Label, Answer
from flask import render_template, abort, request, make_response, jsonify
from database import db
from utils import is_valid_data


def update_one(id):
  if request.method == 'GET':
    question = Question.query\
        .filter_by(question_id = id)\
        .first()
  
    if not question:
      return abort(404)
    
    labels = Label.query.all()
    canEdit = True
    if Answer.query.filter_by(question_id = id).count() > 0:
      canEdit = False
    
    return render_template('update-question.html', question = question, canEdit = canEdit,labels = labels)

  data = request.form

  if not data.get('title') or not data.get('order'):
    print('data', data)
    return make_response("Formulaire invalide.", 400)


  question = Question.query.filter_by(question_id=id).first()
  if not question:
      return make_response("La question n'existe pas.", 404)

  if not data.get('title') or not data.get('order'):
      print('data', data)
      return make_response("Formulaire invalide.", 400)

  print("updating question")
  print(data)

  # Use form data if available, otherwise retain existing data
  question.intro = data.get('intro', question.intro)
  question.past_intro = data.get('past_intro', question.past_intro)
  question.title = data.get('title', question.title)
  question.past_title = data.get('past_title', question.past_title)
  question.info_bubble_text = data.get('info_bubble_text', question.info_bubble_text)
  question.condition = data.get('condition', question.condition)

  intensity = data.get('intensity', str(question.intensity))
  question.intensity = int(intensity) if intensity.isdigit() else None

  conditional_intensity = data.get('conditional_intensity', question.conditional_intensity)
  if conditional_intensity and not is_valid_data(conditional_intensity):
      print('conditional_intensity', conditional_intensity)
      return make_response("La condition " + conditional_intensity + " est invalide.", 400)

  question.conditional_intensity = conditional_intensity
  question.label_id = data.get('label_id', question.label_id)

  order = data.get('order', str(question.order))
  question.order = int(order) if order.isdigit() else None

  question.type = data.get('type', question.type)
  question.active = 1 if data.get('active') else 0
  question.violence_related = 1 if data.get('violence_related') else 0

  if question.type == 'integer':
      min_value = data.get('min_value', str(question.min_value))
      question.min_value = int(min_value) if min_value.isdigit() else None

      max_value = data.get('max_value', str(question.max_value))
      question.max_value = int(max_value) if max_value.isdigit() else None

  # Ladder values
  ladderC = data.get('ladderC', str(question.ladderC))
  question.ladderC = int(ladderC) if ladderC.isdigit() else None

  ladderE = data.get('ladderE', str(question.ladderE))
  question.ladderE = int(ladderE) if ladderE.isdigit() else None

  ladderV = data.get('ladderV', str(question.ladderV))
  question.ladderV = int(ladderV) if ladderV.isdigit() else None

  question.parent = data.get('parent', question.parent)
  question.red_flag = None  # TODO: Define behavior for red_flag
  question.required = 1 if data.get('required') else 0
  question.reverse_answers = 1 if data.get('reverse_answers') else 0


  print(question)

  db.session.add(question)
  db.session.commit()
  return jsonify(question)

def add_one(id):
  survey_id = id
  labels = Label.query.all()
  if request.method == 'POST':
      data = request.form

      if not data.get('question_id') or not data.get('order') or not data.get('title'):
        return make_response("Formulaire invalide.", 400)

      question = Question()
      question.question_id = data.get('question_id') # TODO add verification for regex, to match it with the right survey id letter start
      # regex_str = r'^{}'.format(survey_id)
      # regex = re.compile(regex_str)

      # if not regex.match(question.question_id):
      #   make_response("Formulaire invalide.", 400)

      if Question.query.filter_by(question_id = question.question_id).first():
        return make_response("Une question existe déja avec le ID", 400)
      
      conditional_intensity = data.get('conditional_intensity')
      if conditional_intensity is not None and is_valid_data(conditional_intensity) == False:
        return make_response("La condition " + conditional_intensity + " est invalide.", 400)
      
      question.survey_id = survey_id
      question.type = data.get('type')
      question.intro = data.get('intro') if data.get('intro') else None
      question.title = data.get('title')
      question.info_bubble_text = data.get('info_bubble_text') if data.get('info_bubble_text') else None
      question.condition = data.get('condition') if data.get('condition') else None
      intensity = data.get('intensity')
      question.intensity = int(intensity) if intensity and intensity.isdigit() else None
      question.conditional_intensity = conditional_intensity
      order = data.get('order')
      question.order = int(order) if order and order.isdigit() else None
      question.active = 0 if not data.get('active') else 1
      question.violence_related = 0 if not data.get('violence_related') else 1
      question.label_id = data.get('label_id') if data.get('label_id') else None
      if question.type == 'integer':
        min_value = data.get('min_value')
        question.min_value = int(min_value) if min_value and min_value.isdigit() else None
        max_value = data.get('max_value')
        question.max_value = int(max_value) if max_value and max_value.isdigit() else None
      ladderC = data.get('ladderC')
      question.ladderC = int(ladderC) if ladderC and ladderC.isdigit() else None
      ladderE = data.get('ladderE')
      question.ladderE = int(ladderE) if ladderE and ladderE.isdigit() else None
      ladderV = data.get('ladderV')
      question.ladderV = int(ladderV) if ladderV and ladderV.isdigit() else None
      question.parent = data.get('parent') if data.get('parent') else None
      question.red_flag = None #TODO: Is it a string?
      question.required = 1 if data.get('required') else 0
      question.reverse_answers = 1 if data.get('reverse_answers') else 0

      db.session.add(question)
      db.session.commit()

      return jsonify(question)

  return render_template('add-question.html',survey_id = survey_id,labels = labels)

def delete_one(id):
    question = Question.query\
        .filter_by(question_id = id)\
        .first()
    
    if not question:
      return make_response("La question n'existe pas.", 404)
    
    # TODO performance wise is count or first() better?
    if Answer.query.filter_by(question_id = id).count() > 0:
      return make_response("La question est associée à des réponses",404)
  
    db.session.delete(question)
    db.session.commit()
    return jsonify(question)