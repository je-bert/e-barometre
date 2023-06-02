from models import Choice, Label, Answer, CustomAnswer, Survey, Question,LabelItem
from flask import abort, jsonify, request




def create(current_user, id):
  data = request.json

  data['req_id'] = id
  data['user_id'] = current_user.user_id



  return jsonify(data), 200