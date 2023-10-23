#import dash_core_components as dcc #Deprecated
from dash import dcc
#import dash_html_components as html #Deprecated
from dash import html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
from pathlib import Path
import numpy as np

# get relative data folder
PATH = Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

#Maternal Mortality Rate Data
mmr_file_path = Path(__file__).parent.parent / 'data' / '2.social' / 'maternalMortality' / 'API_SH.STA.MMRT_DS2_en_csv_v2_5872348.csv'
df_mmr = pd.read_csv(mmr_file_path,skiprows=3)
mozambique_data = df_mmr[df_mmr['Country Name'] == 'Mozambique']
# Extract the years and GDP values from the dataframe
years_mmr = list(mozambique_data.columns[43:])
mmr_values = list(mozambique_data.values[0][43:])
#End Maternal Mortality Rate Data

#Literacy Rate Data
litr_file_path = Path(__file__).parent.parent / 'data' / '2.social' / 'literacyRate' / 'API_SE.ADT.LITR.ZS_DS2_en_csv_v2_5871613.csv'
df_litr = pd.read_csv(litr_file_path,skiprows=3)
mozambique_data = df_litr[df_litr['Country Name'] == 'Mozambique']

# # Extract the years and GDP values from the dataframe
years_litr = list(mozambique_data.columns[24:])
litr_values = list(mozambique_data.values[0][24:])


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    html.H6("List of Social Indicators", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]),
                    html.P("Human Development Index (HDI)", style={"font-size": "10px", "color": "#888"}),
                    html.P("Gender wage gap", style={"font-size": "10px", "color": "#888"}),
                    html.P("Violence against women", style={"font-size": "10px", "color": "#888"}),
                    html.P("Food availability", style={"font-size": "10px", "color": "#888"}),
                    html.P("Undernourished people", style={"font-size": "10px", "color": "#888"}),
                    html.P("Children under 5 who are stunted", style={"font-size": "10px", "color": "#888"}),
                    html.P("Food insecure people", style={"font-size": "10px", "color": "#888"}),
                    html.P("Prevalence of food insecure in total population (%)", style={"font-size": "10px", "color": "#888"}),
                    html.P("Access to primary care health services", style={"font-size": "10px", "color": "#888"}),
                    html.P(html.A("Maternal mortality rate", href='#row1', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P("Under-five mortality rate/ Infant mortality rate", style={"font-size": "10px", "color": "#888"}),
                    html.P("Life expectancy",  style={"font-size": "10px", "color": "#888"}),
                    html.P("HIV prevalence", style={"font-size": "10px", "color": "#888"}),
                    html.P(html.A("Literacy rate", href='#row1', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P("Enrollment rates", style={"font-size": "10px", "color": "#888"}),
                    html.P("Educational attainment", style={"font-size": "10px", "color": "#888"}),
                    html.P("Primary school completion rate", style={"font-size": "10px", "color": "#888"}),
                    html.P("Female labor force participation rate", style={"font-size": "10px", "color": "#888"}),
                    html.P("Political representation", style={"font-size": "10px", "color": "#888"}),
                    html.P("Violence against women", style={"font-size": "10px", "color": "#888", }),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin                   

                    html.Br([]),html.Br([]),                    

                    # Row 1
                    html.Div(
                        [
                            html.Div([
                                        html.H6("Maternal mortality ratio (modeled estimate, per 100,000 live births)", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-1",
                                            figure={
                                                "data": [
                                                    go.Scatter(
                                                        x=years_mmr,
                                                        y=mmr_values,
                                                        line={"color": "#97151c"},
                                                        marker=dict(size=3),
                                                        mode="lines+markers",
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
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            18.6880162434,
                                                            278.431996757,
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": False,
                                                    },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                        html.P([
                                                html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                                html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                                html.A("Source: World Bank", href='https://data.worldbank.org/indicator/SH.STA.MMRT?end=2020&locations=MZ&start=2000&view=chart', target="_blank", style={"font-size": "10px", "color": "#888"})
                                            ]),
                                        #html.P(),
                                        
                                ],
                                        className = "six columns",
                            ),
                            html.Div([  
                                        html.H6("Literacy rate, adult total (% of people ages 15 and above)", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-2",
                                            figure={
                                                "data": [
                                                    go.Bar(
                                                        x=years_litr,
                                                        y=litr_values,
                                                        marker={
                                                        "color": "#97151c",
                                                        },                                                        
                                                        # name="",
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
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            18.6880162434,
                                                            278.431996757,
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": True,
                                                    },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                        html.P([
                                                html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                                html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                                html.A("Source: World Bank", href='https://data.worldbank.org/indicator/SE.ADT.LITR.ZS?end=2021&locations=MZ-ZA&name_desc=false&start=1980&view=chart', target="_blank", style={"font-size": "10px", "color": "#888"})
                                                ]),

                                ],
                                    className="six columns"
                            ),

                        ],
                            id = "row1",    
                            className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
        id = "top",
    )
