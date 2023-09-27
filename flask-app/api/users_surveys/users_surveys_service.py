from models import UserSurvey,Survey,Answer
from flask import abort, jsonify, request
from database import db
from api.results import generate

def get_next(current_user):
  completed_surveys = UserSurvey.query\
    .filter_by(user_id = current_user.user_id)\
    .all()
  
  is_user_single = get_is_user_single(current_user)

  kid_potentially_went_to_other_parent_house = get_kid_potentially_went_to_other_parent_house(current_user)



  surveys = Survey.query\
    .filter(Survey.survey_id.notin_([s.survey_id for s in completed_surveys]))

  
  if is_user_single:
    surveys= surveys.filter(Survey.survey_id != 'NC')

  if kid_potentially_went_to_other_parent_house == False:

    surveys= surveys.filter(Survey.survey_id != 'PCRB')



  surveys = surveys.all()



  
  
  if len(surveys) == 0:
    return jsonify({'message':'Done','user_id':current_user.user_id}), 200



  return jsonify(surveys[0]), 200

def get_is_user_single(current_user):

  answer = Answer.query\
    .filter_by(user_id = current_user.user_id)\
    .filter_by(question_id = 'B07')\
    .first()



  if answer:
    return answer.value == '1'
  
  return False 

# TODO (simon) -> Refactor this one
def get_kid_potentially_went_to_other_parent_house(current_user):

  print(Answer.query.filter_by(user_id = current_user.user_id).filter_by(question_id='E32').all())

  first_answer = Answer.query\
    .filter_by(user_id = current_user.user_id)\
    .filter_by(question_id = 'E27')\
    .first()

  second_answer = Answer.query\
    .filter_by(user_id = current_user.user_id)\
    .filter_by(question_id = 'E04')\
    .first()

  third_answer = Answer.query\
    .filter_by(user_id = current_user.user_id)\
    .filter_by(question_id = 'E32')\
    .first()

  if first_answer and first_answer.value and int(first_answer.value) >= 4:
    return True 
  
  if second_answer and second_answer.value and int(second_answer.value) >= 4:
    return True 

  if third_answer and third_answer.value and int(third_answer.value) >= 4:
    return True

  return False



def create(current_user):
  data = request.json


  user_id = current_user.user_id

  survey_id = data['survey_id']

  is_complete = data['is_complete']
  
  user_survey = UserSurvey(user_id=user_id, survey_id=survey_id, is_complete=is_complete)
  
  db.session.add(user_survey)
  
  db.session.commit()
  



  return jsonify({"message":"ok"}), 200