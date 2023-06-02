from models import UserSurvey
from flask import abort, jsonify, request
from database import db

def get_next(current_user):
  completed_surveys = UserSurvey.query\
    .filter_by(user_id = current_user.user_id)\
    .all()

  surveys = Survey.query\
    .filter(Survey.survey_id.notin_([s.survey_id for s in completed_surveys]))\
    .all()
  
  if len(surveys) == 0:
    return abort(404)



  return jsonify(surveys[0]), 200




def create(current_user):
  data = request.json


  user_id = current_user.user_id

  survey_id = data['survey_id']

  is_complete = data['is_complete']
  
  user_survey = UserSurvey(user_id=user_id, survey_id=survey_id, is_complete=is_complete)
  
  db.session.add(user_survey)
  
  db.session.commit()
  



  return jsonify({"message":"ok"}), 200