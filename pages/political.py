#import dash_core_components as dcc #Deprecated
from dash import dcc
#import dash_html_components as html #Deprecated
from dash import html
import plotly.graph_objs as go
#import plotly.express as px
from utils import Header, make_dash_table
import pandas as pd
import pathlib
from pathlib import Path


#load political excel file
file_path = Path(__file__).parent.parent / 'data' / '3.political' / 'political.xlsx'
df_political_stability = pd.read_excel(file_path, sheet_name='political_stability')
df_political_stability_positive = df_political_stability[df_political_stability['value'] > 0]
df_political_stability_negative = df_political_stability[df_political_stability['value'] < 0]
df_rule_of_law = pd.read_excel(file_path, sheet_name='rule_of_law')
df_corruption_index = pd.read_excel(file_path, sheet_name='corruption_index')
df_democracy_index = pd.read_excel(file_path, sheet_name='democracy_index')
df_civil_liberties_index = pd.read_excel(file_path, sheet_name='civil_liberties_index')
df_democratic_culture_index = pd.read_excel(file_path, sheet_name='democratic_culture_index')


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    html.H6("Annually Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    # Row 1
                    html.Div(
                        [
                            html.Div([
                                        html.H6("Political Stability and Absence of Violence/Terrorism: Estimate", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-1",
                                            figure={
                                                "data": [
                                                    go.Scattergl(
                                                        x=df_political_stability_positive['year'],
                                                        y=df_political_stability_positive['value'],
                                                        fill='tozeroy',  # This fills the area below the line to the y-axis
                                                        line={"color": "#97151c"},
                                                        mode="lines",
                                                        name="",
                                                    ),
                                                    go.Scattergl(
                                                        x=df_political_stability_negative['year'],
                                                        y=df_political_stability_negative['value'],
                                                        fill='tozeroy',  # This fills the area below the line to the y-axis
                                                        line={"color": "#97151c"},
                                                        mode="lines",
                                                        name="",
                                                    ),
                                                    # Add more traces if needed for additional stacked areas
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
                                                                    "count": 15,
                                                                    "label": "15Y",
                                                                    "step": "year",
                                                                },
                                                                {
                                                                    "count": 20,
                                                                    "label": "20Y",
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
                                                        "zeroline": True,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            0,  # Adjust the y-axis range according to your data
                                                            500,  # Adjust the y-axis range according to your data
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": True,
                                                    },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                        html.P(html.A("Source: ceicdata", href='https://www.ceicdata.com/en/mozambique/country-governance-indicators', target="_blank", style={"font-size": "10px", "color": "#888"})),                                        
                                ],
                                        className = "six columns",
                            ),
                            html.Div([  
                                        html.H6("Corruption Index", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-2",
                                            figure={
                                                "data": [
                                                    go.Bar(
                                                        x=df_corruption_index['year'],
                                                        y=df_corruption_index['value'],
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
                                                        "autorange": False,
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
                                        html.P(html.A("Source: Trading Economics", href='https://tradingeconomics.com/mozambique/corruption-index', target="_blank", style={"font-size": "10px", "color": "#888"})),

                                ],
                                    className="six columns"
                            ),

                        ],
                                className="row",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Democracy index", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_democracy_index["year"],
                                                    y=df_democracy_index["value"],
                                                    line={"color": "#97151c"},
                                                    mode="lines+markers",
                                                    name="Calibre Index Fund",
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
                                    html.P(html.A("Source: https://ourworldindata.org", href='https://ourworldindata.org/grapher/democracy-index-eiu?tab=chart&country=MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})),
                                ],
                                    className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6("Rule of Law: Estimate", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_rule_of_law["year"],
                                                    y=df_rule_of_law["value"],
                                                    line={"color": "#97151c"},
                                                    mode="lines+markers",
                                                    name="Calibre Index Fund",
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
                                    html.P(html.A("Source: https://data.worldbank.org", href='https://data.worldbank.org/indicator/RL.EST?end=2021&locations=MZ&start=1996&view=chart', target="_blank", style={"font-size": "10px", "color": "#888"})),
                                ],
                                    className="six columns",
                            ),                            
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Democratic Culture Index", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_democratic_culture_index["year"],
                                                    y=df_democratic_culture_index["value"],
                                                    line={"color": "#97151c"},
                                                    mode="lines+markers",
                                                    name="Calibre Index Fund",
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
                                    html.P(html.A("Source: https://ourworldindata.org", href='https://ourworldindata.org/grapher/democratic-culture-index-eiu?tab=chart&country=MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})),
                                ],
                                    className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6("Civil Liberties Index", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_civil_liberties_index["year"],
                                                    y=df_civil_liberties_index["value"],
                                                    line={"color": "#97151c"},
                                                    mode="lines+markers",
                                                    name="Calibre Index Fund",
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
                                    html.P(html.A("Source: https://ourworldindata.org", href='https://ourworldindata.org/grapher/civil-liberties-index-eiu?tab=chart&country=MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})),
                                ],
                                    className="six columns",
                            ),                            
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
