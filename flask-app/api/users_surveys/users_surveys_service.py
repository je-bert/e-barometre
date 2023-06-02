from models import UserSurvey
from flask import abort, jsonify, request
from database import db



def create(current_user):
  data = request.json


  user_id = current_user.user_id

  survey_id = data['survey_id']

  is_complete = data['is_complete']
  
  user_survey = UserSurvey(user_id=user_id, survey_id=survey_id, is_complete=is_complete)
  
  db.session.add(user_survey)
  
  db.session.commit()
  



  return jsonify({"message":"ok"}), 200