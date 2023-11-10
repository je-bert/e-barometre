from models import UserSurvey,Survey,Answer, Report
from flask import abort, jsonify, request
from database import db
from api.results import generate
from api.invoices.invoices_service import get_user_subscription

def get_next(current_user):

  report = Report.query\
    .filter_by(user_id = current_user.user_id, is_completed = False)\
    .first()
  
  current_subscription = get_user_subscription(current_user.user_id)
  
  if current_subscription != 'multiple' :
    completed_reports = Report.query\
      .filter_by(user_id = current_user.user_id, is_completed = True, is_current_subscription = True)\
      .all()
    if len(completed_reports) > 0:
      return jsonify({"survey_id": None}), 200
    
  if current_subscription == None:
    completed_reports = Report.query\
      .filter_by(user_id = current_user.user_id, is_completed = True)\
      .all()
    if len(completed_reports) > 0:
      return jsonify({"survey_id": None}), 200
    return jsonify(None), 200
  
  if not report:
      report = Report(
        user_id = current_user.user_id,
        name = 'Rapport de {} {}'.format(current_user.first_name, current_user.last_name),
        date_created = db.func.current_timestamp(),
      )
      db.session.add(report)
      db.session.commit()

  completed_surveys = UserSurvey.query\
    .filter_by(report_id = report.report_id)\
    .all()
  
  is_user_single = get_is_user_single(report.report_id)

  kid_potentially_went_to_other_parent_house = get_kid_potentially_went_to_other_parent_house(report.report_id)

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

def get_is_user_single(report_id):

  answer = Answer.query\
    .filter_by(report_id = report_id)\
    .filter_by(question_id = 'B08')\
    .first()

  if answer:
    return answer.value == '1'
  
  return False 

# TODO (simon) -> Refactor this one
def get_kid_potentially_went_to_other_parent_house(report_id):

  first_answer = Answer.query\
    .filter_by(report_id = report_id)\
    .filter_by(question_id = 'E27')\
    .first()

  second_answer = Answer.query\
    .filter_by(report_id = report_id)\
    .filter_by(question_id = 'E04')\
    .first()

  third_answer = Answer.query\
    .filter_by(report_id = report_id)\
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

  report = Report.query\
    .filter_by(user_id = current_user.user_id, is_completed = False)\
    .first()
    
  if not report:
    return jsonify({'message':'Aucun rapport en cours.'}), 400

  survey_id = data['survey_id']

  is_complete = data['is_complete']
  
  user_survey = UserSurvey(report_id=report.report_id, survey_id=survey_id, is_complete=is_complete)
  
  db.session.add(user_survey)
  
  db.session.commit()
  

  return jsonify({"message":"ok"}), 200