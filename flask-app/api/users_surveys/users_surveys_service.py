from models import User_Survey
from flask import abort, jsonify, request



def create(current_user):
  data = request.json


  user_id = current_user.user_id

  survey_id = data['survey_id']

  is_complete = data['is_complete']
  
  user_survey = User_Survey(user_id=user_id, survey_id=survey_id, is_complete=is_complete)
  
  user_survey.save()



  return jsonify({"message":"ok"}), 200