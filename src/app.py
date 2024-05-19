#from dbfread import DBF
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import os

# Read data
#dbf = DBF(os.path.abspath('data/Municipalities_with_topo.dbf'), encoding='utf-8')
#df = pd.DataFrame(iter(dbf))
df = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','data', 'Municipalities_with_topo.csv'))

app = Dash(__name__)
server = app.server

# Lista de variables
vars = df.columns[5:]

# Lista de etiquetas etiquetas
variable_options = [
    {'label': 'Tri Mean', 'value': 'tri1k_mean'},
    {'label': 'VRM Mean', 'value': 'vrm1k_mean'},
    {'label': 'ROU Mean', 'value': 'rou1k_mean'},
    {'label': 'SLP Mean', 'value': 'slp1k_mean'},
    {'label': 'Tri Sd', 'value': 'tri1k_sd'},
    {'label': 'VRM Sd', 'value': 'vrm1k_sd'},
    {'label': 'ROU Sd', 'value': 'rou1k_sd'},
    {'label': 'SLP Sd', 'value': 'slp1k_sd'},
]

# Diccionario de etiquetas
label_map = {option['value']: option['label'] for option in variable_options}

app.layout = html.Div([
    html.H4('Matrix Correlations'),
    html.Div([
        html.Label('Select Variables for Scatter Matrix:'),
        dcc.Dropdown(
            id="dropdown_scatter",
            options=variable_options,
            value=['tri1k_mean', 'vrm1k_mean', 'rou1k_mean', 'slp1k_mean'],
            multi=True,
            style={'width': '80%'}
        ),
    ], style={'width': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'margin-bottom': '20px'}),
    
    html.Div([
        html.H5('Scatter Matrix Plot'),
        dcc.Graph(id="scatter_matrix", style={'height': '80vh'})
    ], style={'width': '100%', 'display': 'flex', 'justify-content': 'center', 'flexDirection': 'column', 'align-items': 'center'}),
    
    html.H4('Strip Plot'),
    html.Div([   
        html.Label('Select Variable for Strip Plot:'),
    
        dcc.Dropdown(
            id="dropdown_strip",
            options=variable_options,
            value='tri1k_mean',
            multi=False,
            style={'width': '40%'}
        ),
    ], style={'width': '100%', 'display': 'flex', 'justify-content': 'center','align-items': 'center', 'margin-bottom': '20px'}),
    
    html.Div([
        dcc.Graph(id="strip_plot", style={'height': '70vh'})
    ], style={'width': '100%', 'display': 'flex', 'justify-content': 'center', 'flexDirection': 'column', 'align-items': 'center'})
])


@app.callback(
    Output("scatter_matrix", "figure"),
    [Input("dropdown_scatter", "value")]
)
def update_scatter_matrix(dims):
    fig = px.scatter_matrix(
        df,
        dimensions=dims,
        labels={dim: label_map[dim] for dim in dims}
    )
    fig.update_traces(diagonal_visible=False)
    return fig

@app.callback(
    Output("strip_plot", "figure"),
    [Input("dropdown_strip", "value")]
)
def update_strip_plot(dim):
    fig2 = px.strip(df,
                    x=dim,
                    hover_name="NOMGEO",
                    color="CVE_ENT",
                    height=500,
                    labels={dim: label_map[dim]}
    )
    return fig2

if __name__ == "__main__":
    app.run_server(debug=True,port=8072)
    #http://127.0.0.1:8072/