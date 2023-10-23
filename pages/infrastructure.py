#import dash_html_components as html #Deprecated
from dash import html, dcc
from utils import Header, make_dash_table
import pandas as pd
import pathlib
from pathlib import Path
import plotly.graph_objs as go

# get relative data folder
#PATH = pathlib.Path(__file__).parent
DATA_PATH = Path(__file__).parent.parent / 'data' / '4.infrastructure' / 'infrastructure.xlsx'
#DATA_PATH = DATA_PATH.joinpath("")
df_internet = pd.read_excel(DATA_PATH, sheet_name = 'internet')
df_mobile = pd.read_excel(DATA_PATH, sheet_name = 'cellphone')

def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div([
                    html.H6("List of Infrastructure Indicators", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]),
                    html.P("Road networks", style={"font-size": "10px", "color": "#888"}),
                    html.P("Toll gates network", style={"font-size": "10px", "color": "#888"}),
                    html.P("Urban Mobility Index", style={"font-size": "10px", "color": "#888"}),
                    html.P(html.A("Mobile network coverage", href='#row1', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Internet penetration", href='#row1', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P("Health facilities", style={"font-size": "10px", "color": "#888"}),
                    html.P("Water infrastructures", style={"font-size": "10px", "color": "#888"}),
                    html.P("Irrigation infrastructures", style={"font-size": "10px", "color": "#888"}),
                    html.Br([]),html.Br([]),
                    html.H6("Annually Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Div(
                        [
                            html.Div([
                                        html.H6("Access to Internet from 1990 to 2021", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-1",
                                            figure={
                                                "data": [
                                                    go.Bar(
                                                        x=df_internet['year'],
                                                        y=df_internet['value'],
                                                        marker={
                                                        "color": "#97151c",
                                                        
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                        },
                                                    name="",
                                                    ),
                                                ],
                                                "layout": go.Layout(
                                                    autosize=True,
                                                     width=340,
                                                     height=200,
                                                    font={"family": "Raleway", "size": 10},
                                                    margin={
                                                        "r": 30,
                                                        "t": 30,
                                                        "b": 30,
                                                        "l": 30,
                                                    },
                                                    legend={
                                                    "x": -0.0428945952895,
                                                    "y": -0.209563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                    },
                                                    showlegend=False,
                                                    titlefont={
                                                        "family": "Raleway",
                                                        "size": 10,
                                                    },
                                                    xaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            "2007-12-31",
                                                            "2018-03-06",
                                                        ],
                                                        "rangeselector": {
                                                            "buttons": [
                                                                {
                                                                    "count": 5,
                                                                    "label": "5Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 10,
                                                                    "label": "10Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },                                                                
                                                                {
                                                                    "label": "All",
                                                                    "step": "all",
                                                                },
                                                            ]
                                                        },
                                                        "showline": False,
                                                        "type": "date",
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            22,
                                                            32,
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": False,
                                                        "title": "",
                                                    },
                                                ),
                                            },

                                            config={"displayModeBar": False},
                                        ),
                                        html.P(html.A("Source: https://www.dadosmundiais.com", href='https://www.dadosmundiais.com/africa/mocambique/telecomunicacoes.php', target="_blank", style={"font-size": "10px", "color": "#888"})),                                        
                                ],
                                        className = "six columns",
                            ),
                            html.Div([  
                                        html.H6("Cellphone coverage from 1990 to 2021", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-2",
                                            figure={
                                                "data": [
                                                    go.Bar(
                                                        x=df_mobile['year'],
                                                        y=df_mobile['value'],
                                                        marker={
                                                        "color": "#97151c",
                                                        
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                        },
                                                    name="",
                                                    ),
                                                ],
                                                "layout": go.Layout(
                                                    autosize=True,
                                                     width=340,
                                                     height=200,
                                                    font={"family": "Raleway", "size": 10},
                                                    margin={
                                                        "r": 30,
                                                        "t": 30,
                                                        "b": 30,
                                                        "l": 30,
                                                    },
                                                    legend={
                                                    "x": -0.0428945952895,
                                                    "y": -0.209563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                    },
                                                    showlegend=False,
                                                    titlefont={
                                                        "family": "Raleway",
                                                        "size": 10,
                                                    },
                                                    xaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            "2007-12-31",
                                                            "2018-03-06",
                                                        ],
                                                        "rangeselector": {
                                                            "buttons": [
                                                                {
                                                                    "count": 5,
                                                                    "label": "5Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 10,
                                                                    "label": "10Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },                                                                
                                                                {
                                                                    "label": "All",
                                                                    "step": "all",
                                                                },
                                                            ]
                                                        },
                                                        "showline": False,
                                                        "type": "date",
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            22,
                                                            32,
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": False,
                                                        #"overlaying": "y2",
                                                        "title": "",
                                                    },
                                                    # yaxis2={
                                                    #     "autorange": False,
                                                    #     "range": [-30, 10],
                                                    #     "showgrid": False,
                                                    #     "showline": False,
                                                    #     "title": "Annual % change",
                                                    #     "side": "right",
                                                    #     "type": "linear",
                                                    #     "zeroline": False,
                                                    # },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                        html.P(html.A("Source: https://www.dadosmundiais.com", href='https://www.dadosmundiais.com/africa/mocambique/telecomunicacoes.php', target="_blank", style={"font-size": "10px", "color": "#888"})),

                                ],
                                    className="six columns"
                            ),

                        ],
                                className="row",
                                id="row1",
                    ),
            ],
            className="sub_page",
            ),
        ],
        className="page",
    )
