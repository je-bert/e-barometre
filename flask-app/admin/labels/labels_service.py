from models import Label, LabelItem
from flask import render_template, abort, request, make_response, jsonify
from database import db

def find_all():
  labels = Label.query.all()
  return render_template('labels.html', labels = labels)

def find_one(id):
  label = Label.query\
        .filter_by(label_id = id)\
        .first()
  
  if not label:
    return abort(404)

  label_items = LabelItem.query\
        .filter_by(label_id = id)\
        .all()
  
  return render_template('label.html', label = label, label_items = label_items)


def update_one(id):
  if request.method == 'GET':
    label = Label.query\
        .filter_by(label_id = id)\
        .first()
  
    if not label:
      return abort(404)
    
    return render_template('update-label.html', label = label)

  data = request.form

  if not data.get('label') or not data.get('value'):
    return make_response("Forumulaire invalide.", 400)

  label = Label.query\
        .filter_by(label_id = id)\
        .first()

  if not label:
    return make_response("L'échelle n'existe pas.", 404)

  label.label = data.get('label')
  label.value = data.get('value')
  db.session.commit()
  return jsonify(label)
