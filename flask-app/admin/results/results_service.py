from flask import render_template, send_file, abort
from models import User, AnalysisSection, AnalysisSubsection
import os
from database import db
from pycel import ExcelCompiler


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
  
  filename = 'master_results/{}.xlsx'.format(user_id)

  if not os.path.exists(filename):
    return abort(404)
  
  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  sections = db.session.query(AnalysisSection)\
    .join(AnalysisSubsection)\
    .order_by(AnalysisSection.order)\
    .all()
  
  excel = ExcelCompiler(filename=filename)

  sections_to_render = []

  for section in sections:
    subsections = []
    for subsection in section.subsections:
      subsections.append(render_template('analysis-subsection.html', subsection = subsection, content = generate_content(subsection.schema_type, excel)))
    sections_to_render.append(render_template('analysis-section.html', section = section, subsections = subsections))

  return render_template('user-results.html', user = user, sections_to_render = sections_to_render)

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

def generate_content(type, excel):
  if type == "coparenting-dynamics":
    cl = excel.evaluate("'TEST_pour PROTOTYPE'!D425") / excel.evaluate("'TEST_pour PROTOTYPE'!G425")
    css = excel.evaluate("'TEST_pour PROTOTYPE'!D426") / excel.evaluate("'TEST_pour PROTOTYPE'!G426")
    ap = excel.evaluate("'TEST_pour PROTOTYPE'!D427") / excel.evaluate("'TEST_pour PROTOTYPE'!G427")
    flag = excel.evaluate("'TEST_pour PROTOTYPE'!I428")
    return render_template('charts/barometers.html', cl = cl, css = css, ap = ap, flag = flag)
  elif type == "child-faced-behaviors-index":
    big_value = excel.evaluate("'TEST_pour PROTOTYPE'!C453") / excel.evaluate("'TEST_pour PROTOTYPE'!I453")
    small_value = excel.evaluate("'TEST_pour PROTOTYPE'!C454") / excel.evaluate("'TEST_pour PROTOTYPE'!I454")
    return render_template('charts/double-barometers.html', id = type, big = {"title": "PA", "tooltip": "Indice de sévérité chez les parents", "value": big_value}, small = {"title": "NC", "tooltip": "Indice de contribution chez le nouveau|nouvelle conjoint·e", "value": small_value}) 
  elif type == "harmful-behaviors-bubbles":
    series = []
    series.append({
          "name": 'Parent répondant',
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 482)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 482))} for i in range(6)]
    })
    series.append({
          "name": 'Coparent',
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 489)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 489))} for i in range(7)]
    })
    series.append({
          "name": 'Nouveau conjoint·e (lle cas échéant)',
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 497)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 497))} for i in range(5)]
    })
    return render_template('charts/packed-bubbles.html', id = type, series = series)
  elif type == "alienating-behaviors-bubbles":
    series = []
    series.append({
          "name": "Nature des comportements aliénants des parents",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 660)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 660))} for i in range(3)]
    })
    series.append({
          "name": "Nature de la réaction de l'enfant",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 667)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 667))} for i in range(3)]
    })
    return render_template('charts/packed-bubbles.html', id = type, series = series) 
  elif type == "child-response-bubbles":
    series = []
    series.append({
          "name": "Alliance",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 579)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 579))} for i in range(2)]
    })
    series.append({
          "name": "Altération/dévoiement de la réalité",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 582)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 582))} for i in range(2)]
    })
    series.append({
          "name": "Chantage affectif, loyauté, manipulation",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 585)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 585))} for i in range(2)]
    })
    series.append({
          "name": "Dénigrement",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 588)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 588))} for i in range(2)]
    })
    series.append({
          "name": "Interférence temps et/ou communication",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 591)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 591))} for i in range(3)]
    })
    series.append({
          "name": "Interférence lien affectif ou symbolique",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 595)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 595))} for i in range(2)]
    })
    series.append({
          "name": "Parentification",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 598)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 598))} for i in range(2)]
    })
    series.append({
          "name": "Rôle actif, Réponse au CC, r",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 601)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 601))} for i in range(3)]
    })
    return render_template('charts/packed-bubbles.html', id = type, series = series)
  elif type == "child-behaviors-index":
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C646") / excel.evaluate("'TEST_pour PROTOTYPE'!I646")
    return render_template('charts/barometer.html', id = type, value = value, title = "Sévérité")
  elif type == "child-response-to-alienating-behaviors":
     data = []
     for i in range(36):
       value = excel.evaluate("'TEST_pour PROTOTYPE'!Y{}".format(i + 608))
       if isinstance(value, int) and value > 0:
          title = excel.evaluate("'TEST_pour PROTOTYPE'!X{}".format(i + 608))
          data.append({"title": title, "value": value})
     data = sorted(data, key=lambda d: d['value'], reverse=True)
     return render_template('charts/funnel_v3.html', elements = data)
  elif type == "coparenting-convergence-divergence":
     return render_template('charts/barstack.html', elements = {
      "id":type,
      "categories":["Maturité de l'enfant face à ses choix",
                    "L'enfant coome messager de la logisique",
                    "Fait lire les communications à l'enfant",
                    "Impose sa présence hors de son temps de garde",
                    "Liberté du choix de l'enfant",
                    "Prise de décision sans consentement",
                    "Reproche et dénigrement de l'autre devant l'enfant",
                    "Réaction en présence de l'autre parent",
                    "Transport d'objet entre les deux domiciles",
                    "Valeur du co-parent est en compétition",
                    "Exigence de coparentalité",
                    "Interogatoires au retour de garde"],
      "partyA":{
        "name":"Parent répondant",
        "answers":[4,1,4,1,4,2,2,0,7,4,10,1],
      },
      "partyB":{
        "name":"Coparent",
        "answers":[7,7,2,7,0,1,7,7,0,2,10,2],
      }
    })
  elif type == "coparenting-context":
    labels = ['Absent ', 'Faible ','Modéré ', 'Élevé ']
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C462")
    for i in range(len(labels)):
      max = excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 465))
      if (value > max): continue
      min = excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 465))
      return "<div class='flex w-full overflow-x-auto'>" + create_linear_gauge("Risque de conflit du contexte de coparentalité", labels, i + (value - min) / (max - min), center_labels=True) + "</div>"
    return "TODO"
  elif type == "parental-exclusion-index":
    labels = ['Aucune ', 'Faible ','Possible ', 'Probable ']
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C512")
    for i in range(len(labels)):
      max = excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 514))
      if (value > max): continue
      min = excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 514))
      return "<div class='flex w-full overflow-x-auto'>" + create_linear_gauge("Indice d'exclusion parentale", labels, i + (value - min) / (max - min), center_labels=True) + "</div>"
    return "TODO"
  elif type == "child-symptoms":
    labels = ['Jamais ', 'Rarement ','Occasion. ', 'Régul. ', 'Souvent ', 'Tjrs ']
    titles = ["Insomnie", "Anxiété", "Isolement et difficulté à socialiser", "Trouble de l'opposition", "Trouble alimentaire"]
    scale = [0, 1, 2, 4, 7, 10]
    values = []
    for i in range(len(titles)):
      value = {"value": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(531 + i)), "to": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(531 + i)) * -1}
      value['to'] = get_value_from_scale(value['value'] + value['to'], scale)
      value['value'] = get_value_from_scale(value['value'], scale)
      values.append(value)
    return "<div class='flex w-full overflow-x-auto'>" + "".join([create_linear_gauge(titles[i], labels, values[i]['value'], values[i]['to'], down_color='green') for i in range(len(titles))]) + "</div>"
  elif type == "attitudes-during-custody-transfers":
    labels = ['Calme ', 'Neutre ','Enjoué ', 'Taciturne ', 'Anxieux ', 'Agressif ']
    first_value = 0
    second_value = 0
    for i in range(6):
      if excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(547 + i)) == 1:
        first_value = 5 - i
      if excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(547 + i)) == 1:
        second_value = 5 - i
    excel.evaluate("'TEST_pour PROTOTYPE'!C512")
    first = create_linear_gauge("Au départ", labels, first_value)
    second = create_linear_gauge("Au retour", labels, second_value)
    return "<div class='flex w-full overflow-x-auto'>{}{}</div>".format(first, second)
  elif type == "family-relationship-changes":
    titles = ['Relation parent-parent', "Relation enfant et le coparent", "Relation entre l'enfant et le parent répondant", "Relation entre l'enfant et la famille élargie du parent répondant"]
    labels = ['Mauvaise ', 'Faible ', 'Moyenne ', 'Bonne ', 'Très bonne ', 'Excellente ']
    scale = [0, 1, 2, 4, 7, 10]
    values = []
    for i in range(len(titles)):
      value = {"value": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(560 + i)), "to": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(560 + i))}
      value['to'] = get_value_from_scale(value['value'] + value['to'], scale)
      value['value'] = get_value_from_scale(value['value'], scale)
      values.append(value)
    return "<div class='flex w-full overflow-x-auto'>" + "".join([create_linear_gauge(titles[i], labels, values[i]['value'], values[i]['to']) for i in range(len(titles))]) + "</div>"
  else:
     return type
  

import plotly.offline as pyo
import plotly.graph_objs as go

def get_value_from_scale(value, scale):
  i = 1
  while (value > scale[i]): i += 1
  return (i - 1) + (value - scale[i - 1]) / (scale[i] - scale[i - 1])


def create_linear_gauge(title, labels, value, to = -1, down_color = 'red', center_labels = False, chart_width = 200, chart_height = 600):

  # Range safety
  value = min(max(value, 0), len(labels) - 1)
  if to != -1:
     to = min(max(to, 0), len(labels) - 1)

  # Put all elements of the layout together
  layout = {
      'shapes': [{
          'type': 'rect',
          'x0': 0.02,
          'x1': 0.98,
          'y0': 0,
          'y1': len(labels) + (0 if center_labels else -1),
          'xref': 'x1',
          'yref': 'y1'
      }],
      'xaxis1': {
          'domain': [0, 1],
          'range': [0, 1],
          'showgrid': False,
          'showline': False,
          'zeroline': False,
          'showticklabels': False
      },
      'yaxis1': {
          'anchor': 'x1',
          'range': [-0.5, len(labels) + (0 if center_labels else -1) + 0.5],
          'showgrid': False,
          'showline': False,
          'zeroline': False,
          'ticks': '',
          'ticktext': labels,
          'tickvals': [i + (0.5 if center_labels else 0) for i in range(0, len(labels))],
      },
      'autosize': False,
      'width': chart_width,
      'height': chart_height,
      'margin': {'t': 0, 'b': 0},
      'paper_bgcolor': 'rgba(0,0,0,0)',
      'plot_bgcolor': 'rgba(0,0,0,0)'
  }

  if to == value or to == -1:
    color = "#29ABD6"
  elif to < value:
    color = down_color
    orientation = 'down'
  else:
    color = 'green' if down_color == 'red' else 'red'
    orientation = 'up'

  traces = []

  # Draw the marker 'from'
  traces.append(go.Scatter(
      x=[0.5],
      y=[value],
      xaxis='x1',
      yaxis='y1',
      mode='markers',
      marker={'size': 16, 'color': color},
      text=value,
      hoverinfo='text',
      showlegend=False
  ))

  if to != -1 and to != value:
      #Draw the marker 'to'
      traces.append(go.Scatter(
          x=[0.5],
          y=[to],
          xaxis='x1',
          yaxis='y1',
          mode='markers',
          marker={'size': 16, 'color': color, 'symbol': 'triangle-' + orientation},
          text=to,
          hoverinfo='text',
          showlegend=False
      ))

      # Draw a line connecting the markers
      traces.append(
          go.Scatter(
              x=[0.5, 0.5],
              y=[value, to],
              xaxis='x1',
              yaxis='y1',
              mode='lines',
              line={'color': color, 'width': 4},
              showlegend=False
          )
      )

  # Draw ticks
  for i in range(len(labels) - 1):
    traces.append(
        go.Scatter(
            x=[0, 1],
            y=[i + 1, i + 1],
            xaxis='x1',
            yaxis='y1',
            mode='lines',
            line={'color': "rgb(42, 63, 95, 1)", 'width': 2},
            showlegend=False
        )
    )

  fig = go.Figure(data=traces, layout=layout)
  return "<div class='w-full flex flex-col justify-center items-center'><h3 class='font-bold text-center flex items-center grow -mb-8'>" + title + "</h3>" + pyo.plot(fig, include_plotlyjs=True, output_type='div', config={'staticPlot': True}) + "</div>"