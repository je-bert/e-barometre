from models import Label, LabelItem
from flask import render_template, abort, request, make_response, jsonify
from database import db
import re

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

  if not data.get('title'):
    return make_response("Forumulaire invalide.", 400)

  label = Label.query\
        .filter_by(label_id = id)\
        .first()

  if not label:
    return make_response("L'échelle n'existe pas.", 404)

  label.title = data.get('title')
  db.session.commit()
  return jsonify(label)

def add_one():
    
  if request.method == 'POST':
      data = request.form

      if not data.get('title'):
          return make_response("Formulaire invalide.", 400)
      
      if not re.match(r'^E\d[A-Z]$', data.get('label_id')):
        return make_response('Invalid ID format.', 400)
      
      if Label.query.filter_by(label_id = data.get('label_id')).first():
        return make_response("Le ID pour l'échelle existe déjà", 400)
       
      label = Label(title=data.get('title'), label_id=data.get('label_id'))
      db.session.add(label)
      db.session.commit()

      return jsonify(label)

  return render_template('add-label.html')

def delete_one(id):
    label = Label.query\
        .filter_by(label_id = id)\
        .first()
    
    db.session.delete(label)
    db.session.commit()

    labels = Label.query.all()
    return render_template('labels.html', labels = labels)
