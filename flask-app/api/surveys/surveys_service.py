from models import Choice, Label, Answer, CustomAnswer, Survey, Question,LabelItem
from flask import abort, jsonify

def find_all():
  surveys = Survey.query\
        .filter_by(status= 'active')\
        .all()

  if not surveys:
    return abort(400, 'Record not found') 

  return jsonify(surveys), 200

def find_one(current_user, id):
  survey = Survey.query\
        .filter_by(survey_id = id, status = 'active')\
        .first()

  if not survey:
    return abort(404)

  questions = Question.query\
        .filter_by(survey_id = id)\
        .all()



  res = jsonify(survey).json
  res['questions'] = jsonify(questions).json
  # write res to a file to see what it looks like


  

  for question in res['questions']:

    with open('logs.txt', 'a') as f:
      f.write('\n\nQuestion: \n')
      f.write(str(question))
      f.write('\n\n')



    
    choices = []
    
    if question['type'] == 'labeled-ladder':

      with open('logs.txt', 'a') as f:
        f.write('\n\nLabel: \n')
        f.write(str(question['label_id']))
        f.write('\n\n')


      choices = Label.query\
        .join(LabelItem, LabelItem.label_id == Label.label_id)\
        .filter_by(label_id = question['label_id'])\
        .all()

    else:
      choices = Choice.query\
        .filter_by(question_id = question['question_id'])\
        .all()
    if len(choices) > 0:
      question['choices'] = jsonify(choices).json

    answer = Answer.query\
        .filter_by(question_id = question['question_id'], user_id = current_user.user_id)\
        .first()

    if answer != None:
      question['answer'] = answer.value
      if 'custom' in answer.value:
        custom_answer = CustomAnswer.query\
          .filter_by(question_id = question['question_id'], user_id = current_user.user_id)\
          .first()
        if custom_answer != None:
          question['custom_answer'] = custom_answer.value
  return res, 200