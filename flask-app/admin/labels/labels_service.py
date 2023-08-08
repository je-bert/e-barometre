from models import Label, LabelItem,Question
from flask import render_template, abort, request, make_response, jsonify
from database import db

def find_all():
  labels = Label.query.all()

  for label in labels:
    label_items = LabelItem.query\
        .filter_by(label_id = label.label_id)\
        .all()
    label.title = ' / '.join([label_item.label for label_item in label_items])

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


def add_one():
    
  if request.method == 'POST':
      data = request.form

      if not data.get('label_id'):
          return make_response("Formulaire invalide.", 400)
      
      if Label.query.filter_by(label_id = data.get('label_id')).first():
        return make_response("Le ID pour l'échelle existe déjà", 400)
       
      label = Label(label_id=data.get('label_id'))
      db.session.add(label)
      db.session.commit()

      return jsonify(label)

  return render_template('add-label.html')

def delete_one(id):
    label = Label.query\
        .filter_by(label_id = id)\
        .first()
    
    label_item_count = LabelItem.query.filter_by(label_id = id).count()
    if label_item_count > 0:
      return make_response("Il y a des élements dans l'échelle",404)
    
    question_label_count = Question.query.filter_by(label_id = id).count()
    if question_label_count > 0:
      return make_response("Il y a des questions liées l'échelle",404)
    
    if not label:
      return make_response("L'item n'existe pas.", 404)
    
    db.session.delete(label)
    db.session.commit()
    return 'Échelle supprimée'
