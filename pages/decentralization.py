#import dash_core_components as dcc #Deprecated
from dash import dcc
#import dash_html_components as html #Deprecated
from dash import html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / 'data' / '7.decentralization' / 'decent.xlsx'
#DATA_PATH = DATA_PATH.joinpath("")
#print(DATA_PATH)
df_allocation = pd.read_excel(DATA_PATH, sheet_name = 'allocation') 
local_allocation = df_allocation[df_allocation['level'] == 'Local']
#print(local_allocation)

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.H6("Annually Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                            html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                            html.Br([]),
                            # html.Div([
                            #             html.H6("Local Allocation (Millions of MZN)", className="subtitle padded"),
                            #             dcc.Graph(
                            #                 id="graph-1",
                            #                 figure={
                            #                     "data": [
                            #                         go.Scatter(
                            #                             x=local_allocation['year'],
                            #                             y=local_allocation['value'],
                            #                             line={"color": "#97151c"},
                            #                             mode="lines+markers",
                            #                             name="",
                            #                         ),
                            #                     ],
                            #                     "layout": go.Layout(
                            #                         autosize=True,
                            #                          width=340,
                            #                          height=200,
                            #                         font={"family": "Raleway", "size": 10},
                            #                         margin={
                            #                             "r": 30,
                            #                             "t": 30,
                            #                             "b": 30,
                            #                             "l": 30,
                            #                         },
                            #                         showlegend=False,
                            #                         titlefont={
                            #                             "family": "Raleway",
                            #                             "size": 10,
                            #                         },
                            #                         xaxis={
                            #                             "autorange": True,
                            #                             "range": [
                            #                                 "2007-12-31",
                            #                                 "2018-03-06",
                            #                             ],                                                       
                            #                             "showline": False,
                            #                             "type": "date",
                            #                             "zeroline": False,
                            #                         },
                            #                         yaxis={
                            #                             "autorange": True,
                            #                             "range": [
                            #                                 18.6880162434,
                            #                                 278.431996757,
                            #                             ],
                            #                             "showline": False,
                            #                             "type": "linear",
                            #                             "zeroline": False,
                            #                         },
                            #                     ),
                            #                 },
                            #                 config={"displayModeBar": False},
                            #             ),
                            #             html.P(html.A("Source: https://www.sipri.org", href='https://www.sipri.org/databases/milex', target="_blank", style={"font-size": "10px", "color": "#888"})),
                                        
                            #     ],
                            #             className = "six columns",
                            # ),
                            html.Div([  
                                        html.H6("Local Govenrment Budget Allocation", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-2",
                                            figure={
                                                "data": [
                                                    go.Scatter(
                                                        x=local_allocation['year'],
                                                        y=local_allocation['value'],
                                                        line={"color": "#97151c"},
                                                        mode="lines+markers",
                                                        name="Millions of MZN",
                                                    ),
                                                    go.Bar(
                                                        x=local_allocation['year'],
                                                        y=local_allocation['pct'],
                                                        marker={
                                                        "color": "#bbbbbb",
                                                    },
                                                    name="% of Total",
                                                    yaxis="y2",
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
                                                    showlegend=True,
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
                                                        "showline": False,
                                                        "type": "date",
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            3,
                                                            6.5,
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": False,
                                                        "overlaying": "y2",
                                                        "title": "",
                                                    },
                                                    yaxis2={
                                                        "autorange": False,
                                                        "range": [0, 1],
                                                        "showgrid": False,
                                                        "showline": False,
                                                        "title": "",
                                                        "side": "right",
                                                        "type": "linear",
                                                        "tickformat": ".0%",
                                                        "zeroline": False,
                                                },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                        html.P(html.A("Source: PESOE", href='https://mef.gov.mz/index.php/publicacoes/politicas/plano-economico-e-social-e-orcamento-do-estado-pesoe/pesoe-2023/1711-proposta-do-plano-economico-e-social-e-orcamento-do-estado-para-2023/file', target="_blank", style={"font-size": "10px", "color": "#888"})),

                                ],
                                    className="six columns"
                            ),

                        ],
                                #className="row",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Indicator 3", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    #x=df_graph["Date"],
                                                    #y=df_graph["Calibre Index Fund"],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Calibre Index Fund",
                                                ),
                                                go.Scatter(
                                                    #x=df_graph["Date"],
                                                    # y=df_graph[
                                                    #     "MSCI EAFE Index Fund (ETF)"
                                                    # ],
                                                    line={"color": "#b5b5b5"},
                                                    mode="lines",
                                                    name="MSCI EAFE Index Fund (ETF)",
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
                                                showlegend=True,
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
                                                                "count": 1,
                                                                "label": "1Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 3,
                                                                "label": "3Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 5,
                                                                "label": "5Y",
                                                                "step": "year",
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
                                                    "showline": True,
                                                    "type": "date",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        18.6880162434,
                                                        278.431996757,
                                                    ],
                                                    "showline": True,
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Indicator 4"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            # html.Table(
                                            #     make_dash_table(df_avg_returns),
                                            #     className="tiny-header",
                                            # )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Indicator 5"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            # html.Table(
                                            #     make_dash_table(df_after_tax),
                                            #     className="tiny-header",
                                            # )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Indicator 6"],
                                        className="subtitle padded",
                                    ),
                                    # html.Table(
                                    #     make_dash_table(df_recent_returns),
                                    #     className="tiny-header",
                                    # ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
