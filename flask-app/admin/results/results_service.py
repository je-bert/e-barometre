from flask import render_template, send_file, abort, jsonify
from models import User
import os

def find_all():
  if not os.path.exists('master_results'):
    os.makedirs('master_results')
    
  dir = os.getcwd() + '/master_results/'

  results = []

  for path in os.listdir(dir):
      if os.path.isfile(dir + path):
          user = User.query\
            .filter_by(user_id = path.split('.')[0])\
            .first()
          if user:
            results.append({"file": path, "name": user.first_name + " " + user.last_name, "user_id": user.user_id})

  return render_template('results.html', results = results)

def find_one(user_id):

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
    return abort(404)
  
  series = [
    {
        "name": 'Parent répondant',
        "draggable": False,
        "data": []
        
    }, {
      "name": 'Coparent',
      "draggable": False,
      "data": [
        {
          "value": 30,
          "name": 'Déforme les souvenirs',
        },
        {
          "value": 21,
          "name": "Communique fréquemment avec l'enfant lorsqu'il est chez l'autre"
        },
        {
          "value": 20,
          "name": "En compétition avec l'autre pour l'amour de l'enfant"
        },
        {
          "value": 21,
          "name": "Cherche à blesser l'autre"
        },
        {
          "value": 21,
          "name": "L'enfant est assez mature pour choisir"
        },
        {
          "value": 21,
          "name": "Demande à l'enfant de faire les messages"
        }
      ]
    }, {
        "name": 'Nouveau conjoint·e (lle cas échéant)',
        "draggable": False,
        "data": [
        {
          "value": 20,
          "name": "S'impose responsable de la logistique familiale"
        }
      ]
    }
  ]
  packed_bubbles = render_template('charts/packed-bubbles.html', id = 1, series = series)
  funnel = render_template('charts/funnel.html')
  barometer = render_template('charts/barometer.html')
  return render_template('user-results.html', user = user, packed_bubbles = packed_bubbles, funnel = funnel, barometer = barometer)

def export_one(file_name):
  dir = os.getcwd() + '/master_results/'
  if os.path.isfile(dir + file_name):
            return send_file(dir + file_name, as_attachment=True)
  return "Le fichier n'existe pas", 400

def delete_one(file_name):
  dir = os.getcwd() + '/master_results/'
  if os.path.isfile(dir + file_name):
    os.remove(dir + file_name)
    return "Le fichier a été supprimé", 200
  return "Le fichier n'existe pas", 400