from dbfread import DBF
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

dbf = DBF('D:/Documentos/Apps Python/reports/data/Municipalities_with_topo.dbf', encoding='utf-8')
df = pd.DataFrame(iter(dbf))


app = Dash(__name__)
server = app.server in app.py

app.layout = html.Div([
    html.H4('Matrix correlations'),
    dcc.Dropdown(
        id="dropdown",
        options=['tri1k_mean', 'vrm1k_mean', 'rou1k_mean','slp1k_mean'],
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
    return fig

#http://127.0.0.1:8071/
app.run_server(debug=True,port=8071) 