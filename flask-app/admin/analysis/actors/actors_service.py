from models import Barometer, BarometerItem, Theme, Behavior, Section, BarometerActor, Actor
from flask import render_template, abort, request, make_response, jsonify
from database import db

def update_one(id):
  if request.method == 'GET':
    barometer_actor = BarometerActor.query\
        .filter_by(id = id)\
        .first()
    
    barometer = Barometer.query\
        .filter_by(id = barometer_actor.barometer_id)\
        .first()
    
    actor = Actor.query\
      .filter_by(id = barometer_actor.actor_id)\
      .first()
    
    actors = Actor.query\
      .all()
  
    if not barometer_actor or not barometer or not actor:
      return abort(404)
    
    return render_template('analysis/update-actor.html', section_id = barometer.section_id, barometer_actor = barometer_actor, actor = actor, actors = actors)

  data = request.form

  if not data.get('actor'):
    return make_response("Formulaire invalide.", 400)
  
  actor = Actor.query\
    .filter_by(id = data.get('actor'))\
    .first()
  
  if not actor:
    return make_response("L'acteur n'existe pas.", 400)

  barometer_actor = BarometerActor.query\
      .filter_by(id = id)\
      .first()

  if not barometer_actor:
    return make_response("Impossible de trouver l'acteur à modifier.", 400)

  barometer_actor.actor_id = actor.id
  db.session.commit()

  return jsonify(barometer_actor)