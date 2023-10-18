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
#print(DATA_PATH)
df_internet = pd.read_excel(DATA_PATH, sheet_name = 'internet')
df_mobile = pd.read_excel(DATA_PATH, sheet_name = 'cellphone')

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 5
            # html.Div(
            #     [
            #         # Row 1
            #         html.Div(
            #             [
            #            html.Div(
            #                     [
            #                         html.H6(
            #                             ["Internet users in Mozambique"], 
            #                             className="subtitle padded"
            #                         ),
            #                         # html.P(content),
            #                         html.Ul(
            #                             [
            #                                 html.Br([]),
            #                                 html.Li("There were 6.72 million internet users in Mozambique in January 2021"),
            #                                 html.Li("The number of internet users in Mozambique increased by 1.4 million (+25%) between 2020 and 2021."),
            #                                 html.Li("Internet penetration in Mozambique stood at 21.2% in January 2021."),
            #                                 html.Li("Note: The data sourced from social media platforms is not included in the internet user numbers."),
                                         
            #                             ],
            #                             #style={"color": "#7a7a7a"},
            #                             className="bulletps",
            #                             style={
            #                                 "background-color": "#f9f9f9",
            #                                 "padding-bottom": "30px",
            #                             },
            #                         ),
            #                         html.P(html.A("Source: https://datareportal.com", href='https://datareportal.com/reports/digital-2021-mozambique', target="_blank", style={"font-size": "10px", "color": "#888"})),
            #                     ],
            #                     className="twelve columns",
            #                 )
            #             ],
            #             className="row ",
            #         ),
            #         # Row 2
            #         html.Div(
            #             [
            #                 html.Div(
            #                     [
            #                         html.Br([]),
            #                         html.H6(
            #                             ["Mobile connections in Mozambique in 2022"],
            #                             className="subtitle padded",
            #                         ),
            #                         html.Ul(
            #                             [
            #                                 html.Br([]),
            #                                 html.Li([
            #                                     "Data from ",
            #                                     dcc.Link("GSMA Intelligence", href="https://www.gsmaintelligence.com/?utm_source=DataReportal&utm_medium=article&utm_campaign=State_Internet_Connectivity", target="_blank"),
            #                                     " shows that there were 17.14 million cellular mobile connections in Mozambique at the start of 2022."                                                
            #                                 ],),
            #                                 html.Li("However, note that many people around the world make use of more than one mobile connection – for example, they might have one connection for personal use, and another one for work – so it’s not unusual for mobile connection figures to significantly exceed figures for total population."),
            #                                 html.Li("GSMA Intelligence’s numbers indicate that mobile connections in Mozambique were equivalent to 52.5 percent of the total population in January 2022."),
            #                                 html.Li("The number of mobile connections in Mozambique increased by 1.2 million (+7.7 percent) between 2021 and 2022."),                                         
            #                             ],
            #                             className="bulletps",
            #                             style={
            #                                 "color": "#7a7a7a",
            #                                 "background-color": "#f9f9f9",
            #                                 "padding-bottom": "30px",
            #                             },
            #                         ),
            #                         html.P(html.A("Source: https://datareportal.com", href='https://datareportal.com/reports/digital-2021-mozambique', target="_blank", style={"font-size": "10px", "color": "#888"})),
            #                     ],
            #                     className="twelve columns",
            #                 )
            #             ],
            #             className="row ",
            #         ),
            #         # Row 3
            #         html.Div(
            #             [
            #                 # html.Div(
            #                 #     [
            #                 #         html.H6(
            #                 #             ["Realized/unrealized gains as of 01/31/2018"],
            #                 #             className="subtitle tiny-header padded",
            #                 #         )
            #                 #     ],
            #                 #     className=" twelve columns",
            #                 # )
            #             ],
            #             className="row ",
            #         ),
            #         # Row 4
            #         html.Div(
            #             #[
            #             #     html.Div(
            #             #         [html.Table(make_dash_table(df_realized))],
            #             #         className="six columns",
            #             #     ),
            #             #     html.Div(
            #             #         [html.Table(make_dash_table(df_unrealized))],
            #             #         className="six columns",
            #             #     ),
            #             # ],
            #             className="row ",
            #         ),
            #     ],
            #     className="sub_page",
            # ),
            html.Div([
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
                    ),
            ],
            className="sub_page",
            ),
        ],
        className="page",
    )
