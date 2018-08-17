import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
# from flask import request, jsonify

import pandas as pd

# Local Import
from workers.gsheet_reader import authenticate_and_get_data as read_gsheet

app = dash.Dash()
server = app.server

# Store fitness data as data frame
fitness_log = read_gsheet()

df = pd.DataFrame(
  list(fitness_log[1:len(fitness_log)]),
  index = list(range(1,len(fitness_log))),
  columns = fitness_log[0]
  )


def generate_table(dataframe, max_rows = 10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app.layout = html.Div([
  html.H1("Zuz n Dave's Fitness Logs"),
  html.Label('Choose who to view data for'),
  dcc.Dropdown(
    id = 'person_label',
    options = [
      {'label': 'Zuz', 'value': 'Zuzana'},
      {'label' : 'Dave', 'value': 'David'}
    ],
    value = 'Zuzana',
    multi = False
    ),
  html.Div(id = 'output-div')
  ])


@app.callback(
    dash.dependencies.Output(component_id='output-div', component_property='children'),
    [dash.dependencies.Input('person_label', 'value')]
    )
def update_page(person):
  dff = df[df['Person'] == person]
  return generate_table(dff.tail(n=10))


if __name__ == '__main__':
    app.run_server(debug=True)