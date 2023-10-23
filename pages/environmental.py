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
file_path = Path(__file__).parent.parent / 'data' / '5.environmental' / 'moz-co-emissions-per-capita.csv'
df_co2 = pd.read_csv(file_path)

file_path = Path(__file__).parent.parent / 'data' / '5.environmental' / 'moz-access-to-electricity.csv'
df_electricity = pd.read_csv(file_path)


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    html.H6("List of Environmental Indicators", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]),
                    html.P("Number of climate events", style={"font-size": "10px", "color": "#888"}),
                    html.P("Key actions for climate change mitigation", style={"font-size": "10px", "color": "#888"}),
                    html.P("Infrastructures destroyed by climate events and conflicts", style={"font-size": "10px", "color": "#888"}),
                    html.P("Resilient infrastructure construction", style={"font-size": "10px", "color": "#888"}),
                    html.P(html.A("Access to sustainable energy", href='#row1', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Carbon emissions and air quality", href='#row1', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.Br([]),html.Br([]),
                    html.H6("Annually Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    # Row 1
                    html.Div(
                        [
                            html.Div([  
                                        html.H6("CO₂ emissions (in Tonnes, per person)", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-2",
                                            figure={
                                                "data": [
                                                    go.Bar(
                                                        x=df_co2['year'],
                                                        y=df_co2['value'],
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
                                                        "autorange": False,
                                                        "range": [
                                                            "1948-12-31",
                                                            "2013-03-06",
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
                                                                    "count": 25,
                                                                    "label": "25Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 50,
                                                                    "label": "50Y",
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
                                        html.P(html.A("Source: https://ourworldindata.org/", href='https://ourworldindata.org/co2/country/mozambique', target="_blank", style={"font-size": "10px", "color": "#888"})),

                                ],
                                    className="six columns"
                            ),
                            html.Div([  
                                        html.H6("Electricity access", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-2",
                                            figure={
                                                "data": [
                                                    go.Bar(
                                                        x=df_electricity['year'],
                                                        y=df_electricity['value'],
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
                                                                    "count": 25,
                                                                    "label": "25Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 50,
                                                                    "label": "50Y",
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
                                        html.P(html.A("Source: https://ourworldindata.org/", href='https://ourworldindata.org/energy/country/mozambique', target="_blank", style={"font-size": "10px", "color": "#888"})),

                                ],
                                    className="six columns"
                            ),

                        ],
                                className="row",
                                id="row1"
                    ),
                    # Row 2
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6("Democracy index", className="subtitle padded"),
                    #                 dcc.Graph(
                    #                     id="graph-4",
                    #                     figure={
                    #                         "data": [
                    #                             go.Scatter(
                    #                                 x=df_democracy_index["year"],
                    #                                 y=df_democracy_index["value"],
                    #                                 line={"color": "#97151c"},
                    #                                 mode="lines+markers",
                    #                                 name="Calibre Index Fund",
                    #                             ),
                    #                         ],
                    #                         "layout": go.Layout(
                    #                             autosize=True,
                    #                             width=340,
                    #                             height=200,
                    #                             font={"family": "Raleway", "size": 10},
                    #                             margin={
                    #                                 "r": 30,
                    #                                 "t": 30,
                    #                                 "b": 30,
                    #                                 "l": 30,
                    #                             },
                    #                             showlegend=False,
                    #                             titlefont={
                    #                                 "family": "Raleway",
                    #                                 "size": 10,
                    #                             },
                    #                             xaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     "2007-12-31",
                    #                                     "2018-03-06",
                    #                                 ],
                    #                                 "rangeselector": {
                    #                                     "buttons": [
                    #                                         {
                    #                                             "count": 1,
                    #                                             "label": "1Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 3,
                    #                                             "label": "3Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 5,
                    #                                             "label": "5Y",
                    #                                             "step": "year",
                    #                                         },
                    #                                         {
                    #                                             "count": 10,
                    #                                             "label": "10Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "label": "All",
                    #                                             "step": "all",
                    #                                         },
                    #                                     ]
                    #                                 },
                    #                                 "showline": True,
                    #                                 "type": "date",
                    #                                 "zeroline": False,
                    #                             },
                    #                             yaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     18.6880162434,
                    #                                     278.431996757,
                    #                                 ],
                    #                                 "showline": True,
                    #                                 "type": "linear",
                    #                                 "zeroline": False,
                    #                             },
                    #                         ),
                    #                     },
                    #                     config={"displayModeBar": False},
                    #                 ),
                    #                 html.P(html.A("Source: https://ourworldindata.org", href='https://ourworldindata.org/grapher/democracy-index-eiu?tab=chart&country=MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})),
                    #             ],
                    #                 className="six columns",
                    #         ),
                    #         html.Div(
                    #             [
                    #                 html.H6("Rule of Law: Estimate", className="subtitle padded"),
                    #                 dcc.Graph(
                    #                     id="graph-4",
                    #                     figure={
                    #                         "data": [
                    #                             go.Scatter(
                    #                                 x=df_rule_of_law["year"],
                    #                                 y=df_rule_of_law["value"],
                    #                                 line={"color": "#97151c"},
                    #                                 mode="lines+markers",
                    #                                 name="Calibre Index Fund",
                    #                             ),
                    #                         ],
                    #                         "layout": go.Layout(
                    #                             autosize=True,
                    #                             width=340,
                    #                             height=200,
                    #                             font={"family": "Raleway", "size": 10},
                    #                             margin={
                    #                                 "r": 30,
                    #                                 "t": 30,
                    #                                 "b": 30,
                    #                                 "l": 30,
                    #                             },
                    #                             showlegend=False,
                    #                             titlefont={
                    #                                 "family": "Raleway",
                    #                                 "size": 10,
                    #                             },
                    #                             xaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     "2007-12-31",
                    #                                     "2018-03-06",
                    #                                 ],
                    #                                 "rangeselector": {
                    #                                     "buttons": [
                    #                                         {
                    #                                             "count": 1,
                    #                                             "label": "1Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 3,
                    #                                             "label": "3Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 5,
                    #                                             "label": "5Y",
                    #                                             "step": "year",
                    #                                         },
                    #                                         {
                    #                                             "count": 10,
                    #                                             "label": "10Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "label": "All",
                    #                                             "step": "all",
                    #                                         },
                    #                                     ]
                    #                                 },
                    #                                 "showline": True,
                    #                                 "type": "date",
                    #                                 "zeroline": False,
                    #                             },
                    #                             yaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     18.6880162434,
                    #                                     278.431996757,
                    #                                 ],
                    #                                 "showline": True,
                    #                                 "type": "linear",
                    #                                 "zeroline": False,
                    #                             },
                    #                         ),
                    #                     },
                    #                     config={"displayModeBar": False},
                    #                 ),
                    #                 html.P(html.A("Source: https://data.worldbank.org", href='https://data.worldbank.org/indicator/RL.EST?end=2021&locations=MZ&start=1996&view=chart', target="_blank", style={"font-size": "10px", "color": "#888"})),
                    #             ],
                    #                 className="six columns",
                    #         ),                            
                    #     ],
                    #     className="row ",
                    # ),
                    # # Row 3
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6("Democratic Culture Index", className="subtitle padded"),
                    #                 dcc.Graph(
                    #                     id="graph-4",
                    #                     figure={
                    #                         "data": [
                    #                             go.Scatter(
                    #                                 x=df_democratic_culture_index["year"],
                    #                                 y=df_democratic_culture_index["value"],
                    #                                 line={"color": "#97151c"},
                    #                                 mode="lines+markers",
                    #                                 name="Calibre Index Fund",
                    #                             ),
                    #                         ],
                    #                         "layout": go.Layout(
                    #                             autosize=True,
                    #                             width=340,
                    #                             height=200,
                    #                             font={"family": "Raleway", "size": 10},
                    #                             margin={
                    #                                 "r": 30,
                    #                                 "t": 30,
                    #                                 "b": 30,
                    #                                 "l": 30,
                    #                             },
                    #                             showlegend=False,
                    #                             titlefont={
                    #                                 "family": "Raleway",
                    #                                 "size": 10,
                    #                             },
                    #                             xaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     "2007-12-31",
                    #                                     "2018-03-06",
                    #                                 ],
                    #                                 "rangeselector": {
                    #                                     "buttons": [
                    #                                         {
                    #                                             "count": 1,
                    #                                             "label": "1Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 3,
                    #                                             "label": "3Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 5,
                    #                                             "label": "5Y",
                    #                                             "step": "year",
                    #                                         },
                    #                                         {
                    #                                             "count": 10,
                    #                                             "label": "10Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "label": "All",
                    #                                             "step": "all",
                    #                                         },
                    #                                     ]
                    #                                 },
                    #                                 "showline": True,
                    #                                 "type": "date",
                    #                                 "zeroline": False,
                    #                             },
                    #                             yaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     18.6880162434,
                    #                                     278.431996757,
                    #                                 ],
                    #                                 "showline": True,
                    #                                 "type": "linear",
                    #                                 "zeroline": False,
                    #                             },
                    #                         ),
                    #                     },
                    #                     config={"displayModeBar": False},
                    #                 ),
                    #                 html.P(html.A("Source: https://ourworldindata.org", href='https://ourworldindata.org/grapher/democratic-culture-index-eiu?tab=chart&country=MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})),
                    #             ],
                    #                 className="six columns",
                    #         ),
                    #         html.Div(
                    #             [
                    #                 html.H6("Civil Liberties Index", className="subtitle padded"),
                    #                 dcc.Graph(
                    #                     id="graph-4",
                    #                     figure={
                    #                         "data": [
                    #                             go.Scatter(
                    #                                 x=df_civil_liberties_index["year"],
                    #                                 y=df_civil_liberties_index["value"],
                    #                                 line={"color": "#97151c"},
                    #                                 mode="lines+markers",
                    #                                 name="Calibre Index Fund",
                    #                             ),
                    #                         ],
                    #                         "layout": go.Layout(
                    #                             autosize=True,
                    #                             width=340,
                    #                             height=200,
                    #                             font={"family": "Raleway", "size": 10},
                    #                             margin={
                    #                                 "r": 30,
                    #                                 "t": 30,
                    #                                 "b": 30,
                    #                                 "l": 30,
                    #                             },
                    #                             showlegend=False,
                    #                             titlefont={
                    #                                 "family": "Raleway",
                    #                                 "size": 10,
                    #                             },
                    #                             xaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     "2007-12-31",
                    #                                     "2018-03-06",
                    #                                 ],
                    #                                 "rangeselector": {
                    #                                     "buttons": [
                    #                                         {
                    #                                             "count": 1,
                    #                                             "label": "1Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 3,
                    #                                             "label": "3Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 5,
                    #                                             "label": "5Y",
                    #                                             "step": "year",
                    #                                         },
                    #                                         {
                    #                                             "count": 10,
                    #                                             "label": "10Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "label": "All",
                    #                                             "step": "all",
                    #                                         },
                    #                                     ]
                    #                                 },
                    #                                 "showline": True,
                    #                                 "type": "date",
                    #                                 "zeroline": False,
                    #                             },
                    #                             yaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     18.6880162434,
                    #                                     278.431996757,
                    #                                 ],
                    #                                 "showline": True,
                    #                                 "type": "linear",
                    #                                 "zeroline": False,
                    #                             },
                    #                         ),
                    #                     },
                    #                     config={"displayModeBar": False},
                    #                 ),
                    #                 html.P(html.A("Source: https://ourworldindata.org", href='https://ourworldindata.org/grapher/civil-liberties-index-eiu?tab=chart&country=MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})),
                    #             ],
                    #                 className="six columns",
                    #         ),                            
                    #     ],
                    #     className="row ",
                    # ),
                    # # Row 4
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     [
                    #                         "Indicator 5"
                    #                     ],
                    #                     className="subtitle padded",
                    #                 ),
                    #                 html.Div(
                    #                     [
                    #                         # html.Table(
                    #                         #     make_dash_table(df_after_tax),
                    #                         #     className="tiny-header",
                    #                         # )
                    #                     ],
                    #                     style={"overflow-x": "auto"},
                    #                 ),
                    #             ],
                    #             className=" twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                    # # Row 5
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     ["Indicator 6"],
                    #                     className="subtitle padded",
                    #                 ),
                    #                 # html.Table(
                    #                 #     make_dash_table(df_recent_returns),
                    #                 #     className="tiny-header",
                    #                 # ),
                    #             ],
                    #             className=" twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
