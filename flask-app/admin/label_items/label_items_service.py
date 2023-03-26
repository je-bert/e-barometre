from models import LabelItem
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

  order = data.get('order')
  label_item.order = int(order) if order and order.isdigit() else None
  value = data.get('value')
  label_item.value = int(value) if value and value.isdigit() else -1
  label_item.label = data.get('label')
  db.session.commit()
  return jsonify(label_item)