from models import Question, Answer, Choice
from flask import render_template, abort, request, make_response
from database import db
import json
from sqlalchemy.orm import joinedload
from utils import conditional_intensity_parser as cip


def update_one(id):
  if request.method == 'GET':
    question = Question.query\
        .filter_by(question_id = id)\
        .first()
  
    if not question:
      return abort(404)
    
    return render_template('update-question.html', question = question)

  data = request.form

  if not data.get('title'):
    return make_response("Forumulaire invalide.", 400)

  question = Question.query\
        .filter_by(question_id = id)\
        .first()

  if not question:
    return make_response("La question n'existe pas.", 404)

  question.title = data.get('title')
  db.session.commit()
  return question.as_dict()

def generate_gradients(report_id):
  user_answers = db.session.query(Answer).\
    filter(Answer.report_id == report_id).\
    all()
  choices = Choice.query.all()
  choices_dict = {choice.question_id + choice.value: choice for choice in choices}
  gradients = {}
  answers_dict = {answer.question_id: answer for answer in user_answers}
  question_trees = build_question_trees() 
  question_trees = json.loads(question_trees)
  for question_id, question in question_trees.items(): 
    compute_gradient(question_id, question, answers_dict, choices_dict, gradients, question_trees)
  return gradients

def compute_gradient(question_id, question, answers_dict, choices_dict, gradients, question_trees):
  if question_id not in answers_dict:
     return 0
  
  intensity = question['intensity']
  values = answers_dict[question_id].value.split(',')
  if question['conditional_intensity'] is not None:
    conditionnal_intensity = cip.parse_conditional_intensity(question, answers_dict)
    if conditionnal_intensity is not None:
      intensity = conditionnal_intensity
  compute_method = question['intensity_method'] if question['intensity_method'] is not None else "SUM"
  if intensity is None:
    #Get frequency from choice if question does not have intensity
    frequency = 0
    intensity = 1
    for value in values:
      choice = choices_dict.get(question_id + value)
      if choice:
        if compute_method == "SUM":
          frequency += choice.intensity
        elif compute_method == "MAX":
          frequency = max(frequency, choice.intensity)
      else:
        print("Choice not found for question_id: {}, value: {}".format(question_id, value))
  else:
    values = [int(value) for value in values if value.isdigit()]
    frequency = sum(values) if compute_method == "SUM" else max(values)

  gradient = intensity * frequency
  gradients[question_id] = gradient

  # Si la Q n'a pas de sous-question, on prend la valeur de celle-ci
  if 'children' not in question or len(question['children']) == 0:
    return gradient
  
  childrenSum = 0
  for child in question['children']:
    childrenSum += compute_gradient(child['question_id'], child, answers_dict, choices_dict, gradients, question_trees)

  # Prendre le MAX entre Q et chaque niveau de SQ
  gradients["G_" + question_id] = max(childrenSum, gradient)
     
  
  return max(childrenSum, gradient)


class TreeNode:
    def __init__(self, question_id, intensity, intensity_method, conditional_intensity):
        self.question_id = question_id
        self.intensity = intensity
        self.intensity_method = intensity_method
        self.conditional_intensity = conditional_intensity
        

    def add_child(self, child_node):
        if not hasattr(self, 'children'):
            self.children = []
        self.children.append(child_node)

    def to_dict(self):
      return {
         "question_id": self.question_id,
          "children": [child.to_dict() for child in self.children] if hasattr(self, 'children') and self.children else [],
          "intensity": self.intensity,
          "intensity_method": self.intensity_method,
          "conditional_intensity": self.conditional_intensity,
        }

def get_all_questions():
    questions = db.session.query(Question).all()
    child_questions = {}
    root_questions = {}
    for question in questions:
        if question.parent != None:
          child_questions[question.question_id]= question
        else:
          root_questions[question.question_id]= question
    return child_questions, root_questions

def build_question_trees():
    trees = []
    child_questions, root_questions = get_all_questions()
    for question in root_questions.values():
        trees.append(build_node(question, child_questions))
    tree_data = {}
    for tree in trees:
        tree_dict = {
          "question_id": tree.question_id,
          "children": [child.to_dict() for child in tree.children] if hasattr(tree, 'children') and tree.children else [],
          "intensity": tree.intensity,
          "intensity_method": tree.intensity_method,
          "conditional_intensity": tree.conditional_intensity,
        }
        tree_data[tree.question_id] = tree_dict
    return json.dumps(tree_data)

def build_node(question, questions_dict):
    node = TreeNode(question.question_id, question.intensity, question.intensity_method, question.conditional_intensity)
    children = [question for question in questions_dict.values() if question.parent == node.question_id]
    for child in children:
      node.add_child(build_node(child, questions_dict))
    return node