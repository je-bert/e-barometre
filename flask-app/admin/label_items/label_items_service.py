from models import LabelItem,Label,Answer,Question
from flask import render_template, abort, request, make_response, jsonify
from database import db


def update_one(id):
  if request.method == 'GET':
    label_item = LabelItem.query\
        .filter_by(label_item_id = id)\
        .first()
  
    if not label_item:
      return abort(404)
    
    return render_template('update-label-item.html', label_item = label_item)

  data = request.form

  if not data.get('value') or not data.get('label') or not data.get('order'):
    return make_response("Formulaire invalide.", 400)

  label_item = LabelItem.query\
        .filter_by(label_item_id = id)\
        .first()

  if not label_item:
    return make_response("L'item n'existe pas.", 404)

  # TODO, change label for titre? to keep consistency with the html template? or vice versa
  order = data.get('order')
  label_item.order = int(order) if order and order.isdigit() else None
  value = data.get('value')
  label_item.value = int(value) if value and value.isdigit() else -1
  label_item.label = data.get('label')
  db.session.commit()
  return jsonify(label_item)

def add_one(id):
  label_id = id

  last_label_item = LabelItem.query.order_by(LabelItem.label_id.desc(),LabelItem.label_item_id.desc()).first()
  if last_label_item:
    label_item_id = int(last_label_item.label_item_id) + 1
  else:
    label_item_id = 1

  if request.method == 'POST':
      data = request.form

      if not data.get('value') or not data.get('label') or not data.get('order'):
        return make_response("Formulaire invalide.", 400)

      label_item = LabelItem()
      label_item.label_item_id = str(label_item_id)
      label_item.label_id = label_id
      order = data.get('order')
      label_item.order = int(order) if order and order.isdigit() else None
      value = data.get('value')
      label_item.value = int(value) if value and value.isdigit() else -1
      label_item.label = data.get('label')

      db.session.add(label_item)
      db.session.commit()

      return jsonify(label_item)

  return render_template('add-label-item.html',label_id = label_id, label_item_id = label_item_id)

def delete_one(id):
    label_item = LabelItem.query\
        .filter_by(label_item_id = id)\
        .first()
    
    if not label_item:
      return make_response("L'item n'existe pas.", 404)
  
    db.session.delete(label_item)
    db.session.commit()
    return jsonify(label_item)