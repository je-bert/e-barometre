from flask import abort, jsonify, render_template
from models import User, Answer, Question, AnalysisSection, AnalysisSubsection
import os
from database import db
from shutil import copyfile
import os
from openpyxl import load_workbook
from pycel import ExcelCompiler

def generate():
  convert_xlookup_to_index_match()
  user_id = 1

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)
  
  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  template_file = 'Master_TEST_Barometre_230523_8h00_3.xlsx'
  worksheet_name = 'TEST_pour PROTOTYPE'
  output_file = 'master_results/{}.xlsx'.format(user.user_id)
  if not os.path.exists(output_file):
     copyfile(template_file, output_file)

  # Load the workbook and access the sheet we'll paste into
  wb = load_workbook(output_file)
  ws = wb.get_sheet_by_name(worksheet_name)

  answers = Answer.query\
    .filter_by(user_id = user_id)\
    .all()

  for answer in answers:
    question = Question.query\
          .filter_by(question_id = answer.question_id )\
          .first()
    if question.type == 'select-multiple':
      values = answer.value.split(',')
      i = 1
      for cell in ws["C"]:
        if type(cell).__name__ != 'MergedCell' and cell.internal_value == answer.question_id:
          ws.cell(row=cell.row, column=4).value = 1 if str(i) in values else 0
          i += 1
    else:
      for cell in ws["C"]:
        if type(cell).__name__ != 'MergedCell' and cell.internal_value == answer.question_id:
            ws.cell(row=cell.row, column=4).value = answer.value
  
  wb.save(output_file)

  return jsonify("Votre rapport a été généré!"), 200

def output():
  user_id = 1

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)

  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  filename = 'master_results/{}.xlsx'.format(user_id)

  if not os.path.exists(filename):
     return abort(404)
  
  worksheet_name = 'Test de contenu du rapport'

  sections = db.session.query(AnalysisSection)\
    .join(AnalysisSubsection)\
    .order_by(AnalysisSection.order)\
    .all()
  
  excel = ExcelCompiler(filename=filename)

  section_title = None
  sections = []
  subsections = []
  subsection_title = None
  type = None
  about = None
  subsection_description = None
  themes = []
  conclusion = None
  flag_introduction = None
  yellow_flags = []
  red_flags = []

  for i in range (1, 400):
    cell = excel.evaluate(f"'{worksheet_name}'!A{i}")
    if cell and cell != '' and cell != ' ':
      value = excel.evaluate(f"'{worksheet_name}'!B{i}")
      if cell == 'endsubsection':
        sections.append(render_template('reports/themes.html', analysis_items = themes, observations = themes))
        if len(red_flags) > 0 or len(yellow_flags) > 0:
          sections.append(render_template('reports/flags.html', yellow_flags = yellow_flags, red_flags = red_flags))
        themes = []
        yellow_flags = []
        red_flags = []
      elif not value or value == '' or value == ' ' or value == 0:
        continue
      elif cell == 'section':
        sections.append(render_template('reports/section-title.html', content = value))
      elif cell == 'subsection':
        sections.append(render_template('reports/subsection-title.html', content = value))
      elif cell == 'about':
        sections.append(render_template('reports/about-barometer.html', content = value))
      elif cell == 'type':
        sections.append(render_template('reports/report-1/barometer-1.html'))
      elif cell == 'description':
        subsection_description = value
      elif cell == 'ressources':
        sections.append(render_template('reports/ressources.html', content = value))
      elif cell == 'theme':
        themes.append(value)
      elif cell == 'conclusion':
        conclusion = value
      elif cell == 'flag_introduction':
        flag_introduction = value
      elif cell == 'yellow_flag':
        yellow_flags.append(value)
      elif cell == 'red_flag':
        red_flags.append(value)

  return render_template('reports/report-1/base.html', children = sections)

def convert_xlookup_to_index_match():
  filename = 'Master_TEST_Barometre_230523_8h00_3.xlsx'
  sheetname = 'Modèle Calcul A-R + Sommaire'
  cell_range = 'D32:U800'

  # Load the workbook
  workbook = load_workbook(filename)
  worksheet = workbook[sheetname]

  # Get the cell range
  cells = worksheet[cell_range]

  for row in cells:
      for cell in row:
          # Get the formula from the cell
          formula = cell.value
          print(formula)
          # Check if the formula is an XLOOKUP formula
          if formula and not isinstance(formula, int) and  formula.startswith('=_xlfn.XLOOKUP('):
              lookup_args = formula[15:-1].split(',')
              search_value = lookup_args[0].strip()
              lookup_range = lookup_args[1].strip()
              return_range = lookup_args[2].strip()

              # Replace the XLOOKUP formula with INDEX and MATCH formula
              index_match_formula = f'=_xlfn.INDEX({return_range}, _xlfn.MATCH({search_value}, {lookup_range}, 0), 1)'
              cell.value = index_match_formula

  # Save the updated workbook
  workbook.save(filename)
  return "Success",200


def generate_content(type, excel):
  if type == "coparenting-dynamics":
    cl = { "val": excel.evaluate("'TEST_pour PROTOTYPE'!D427") / excel.evaluate("'TEST_pour PROTOTYPE'!G427"), 
          "green_stop": excel.evaluate("'TEST_pour PROTOTYPE'!F427") / excel.evaluate("'TEST_pour PROTOTYPE'!G427")
        }
    css ={ "val": excel.evaluate("'TEST_pour PROTOTYPE'!D428") / excel.evaluate("'TEST_pour PROTOTYPE'!G428"),
          "green_stop": excel.evaluate("'TEST_pour PROTOTYPE'!F428") / excel.evaluate("'TEST_pour PROTOTYPE'!G428")}
    ap = { "val": excel.evaluate("'TEST_pour PROTOTYPE'!D429") / excel.evaluate("'TEST_pour PROTOTYPE'!G429"),
          "green_stop": excel.evaluate("'TEST_pour PROTOTYPE'!F429") / excel.evaluate("'TEST_pour PROTOTYPE'!G429")}
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
    # series.append({
    #       "name": "Alliance",
    #       "draggable": False,
    #       "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 579)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 485))} for i in range(2)]
    # })
    series.append({
          "name": "Altération/dévoiement de la réalité",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 470)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 470))} for i in range(6) if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(i + 470)) == 'à inclure']
    })
    series.append({
          "name": "Chantage affectif, loyauté, manipulation",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 477)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 477))} for i in range(6) if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(i + 477)) == 'à inclure']
    })
    series.append({
          "name": "Dénigrement",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 484)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 484))} for i in range(4) if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(i + 484)) == 'à inclure']
    })
    series.append({
          "name": "Interférence temps et/ou communication",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 489)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 489))} for i in range(9) if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(i + 489)) == 'à inclure']
    })
    series.append({
          "name": "Interférence lien affectif ou symbolique",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 499)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 499))} for i in range(5) if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(i + 499)) == 'à inclure']
    })
    series.append({
          "name": "Parentification",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 505)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 505))} for i in range(4) if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(i + 505)) == 'à inclure']
    })
    series.append({
          "name": "Rôle actif de l'enfant",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(i + 510)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(i + 510))} for i in range(4) if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(i + 510)) == 'à inclure']
    })
    return render_template('charts/packed-bubbles.html', id = type, series = series)
  elif type == "new-parent-contribution":
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C545") / excel.evaluate("'TEST_pour PROTOTYPE'!H545")
    return render_template('charts/barometer.html', id = type, value = value, title = "Indice de contribution chez le nouveau|nouvelle conjoint·e")
  elif type == "child-behaviors-index":
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C646") / excel.evaluate("'TEST_pour PROTOTYPE'!I646")
    return render_template('charts/barometer.html', id = type, value = value, title = "Sévérité")
  elif type == "child-response-to-alienating-behaviors":
     data = []
     for i in range(30):
       value = excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 571))
       if isinstance(value, int) and value > 0:
          title = excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 571))
          data.append({"title": title, "value": value})
     data = sorted(data, key=lambda d: d['value'], reverse=True)
     return render_template('charts/funnel.html', elements = data)
  elif type == "coparenting-convergence-divergence":
    return render_template('charts/barstack.html', elements = {
      "id":type.replace('-', '_'),
      "categories":[excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 455)) for i in range(8)],
      "partyA":{
        "name":"Parent répondant",
        "answers":[excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 455)) for i in range(8)],
      },
      "partyB":{
        "name":"Coparent",
        "answers":[excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 455)) for i in range(8)],
      }
    })
  elif type == "coparenting-child-resentment":
    return render_template('charts/barstack.html', elements = {
      "id":type.replace('-', '_'),
      "categories":[excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 464)) for i in range(5)],
      "partyA":{
        "name":"Parent répondant",
        "answers":[excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 464)) for i in range(5)],
      },
      "partyB":{
        "name":"Coparent",
        "answers":[excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 464)) for i in range(5)],
      }
    })
  elif type == "coparenting-context":
    labels = ['Absent ', 'Faible ','Modéré ', 'Élevé ']
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C438")
    for i in range(len(labels)):
      max = excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 441))
      if (value > max): continue
      min = excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 441))
      return "<div class='flex w-full overflow-x-auto'>" + create_linear_gauge("Risque de conflit du contexte de coparentalité", labels, i + (value - min) / (max - min), center_labels=True) + "</div>"
    return "TODO"
  elif type == "parental-exclusion-index":
    labels = ['Aucune ', 'Faible ','Possible ', 'Probable ']
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C524")
    for i in range(len(labels)):
      max = excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 529))
      if (value > max): continue
      min = excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 529))
      return "<div class='flex w-full overflow-x-auto'>" + create_linear_gauge("Indice d'exclusion parentale", labels, i + (value - min) / (max - min), center_labels=True) + "</div>"
    return "TODO"
  elif type == "child-symptoms":
    labels = ['Jamais ', 'Rarement ','Occasion. ', 'Régul. ', 'Souvent ', 'Tjrs ']
    titles = ["Insomnie", "Anxiété", "Isolement et difficulté à socialiser", "Trouble de l'opposition", "Trouble alimentaire"]
    scale = [0, 1, 2, 4, 7, 10]
    flags = []
    for i in range (3):
      label = excel.evaluate("'TEST_pour PROTOTYPE'!K{}".format(532 + i * 2))
      label = label[0].upper() + label[1:]
      flags.append({"label": label, "value": 1 if excel.evaluate("'TEST_pour PROTOTYPE'!L{}".format(532 + i * 2)) == 1 else 0})
    values = []
    for i in range(len(titles)):
      value = {"value": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(531 + i)), "to": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(531 + i)) * -1}
      value['to'] = get_value_from_scale(value['value'] + value['to'], scale)
      value['value'] = get_value_from_scale(value['value'], scale)
      values.append(value)
    retval = "<div class='flex w-full flex-col'><div class='flex w-full mb-4 items-center shadow-md bg-blue-100 justify-center py-4 sm:space-x-6 flex-col space-y-4 sm:space-y-0 sm:flex-row'>"
    for flag in flags:
      retval += "<div class='flex flex-col text-center'><b>{}</b><p>{}</p></div>".format(flag['label'], "Oui" if flag['value'] == 1 else "Non")
    return retval + "</div><div class='flex w-full overflow-x-auto'>" + "".join([create_linear_gauge(titles[i], labels, values[i]['value'], values[i]['to'], down_color='green') for i in range(len(titles))]) + "</div></div>"
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
