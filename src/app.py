#from dbfread import DBF
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import os

# Read data
#dbf = DBF(os.path.abspath('data/Municipalities_with_topo.dbf'), encoding='utf-8')
#df = pd.DataFrame(iter(dbf))
df = pd.read_csv(os.path.abspath('data/Municipalities_with_topo.csv'))

app = Dash(__name__)
server = app.server

vars = df.columns[5:]

app.layout = html.Div([
    html.H4('Matrix correlations'),
    dcc.Dropdown(
        id="dropdown",
        options=vars,
        value=['tri1k_mean', 'vrm1k_mean', 'rou1k_mean','slp1k_mean'],
        multi=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(dims):
    fig = px.scatter_matrix(
        df, dimensions=dims)
    fig.update_traces(diagonal_visible=False)
    return fig

#http://127.0.0.1:8072/
app.run_server(debug=True,port=8072) 