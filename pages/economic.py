import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go #Added by @MGB

from utils import Header, make_dash_table

import geopandas as gpd
import json
from dash.dependencies import Input, Output
import pandas as pd
from pathlib import Path
from geopandas import GeoDataFrame # Added by @MGB
import matplotlib.pyplot as plt # Added by @MGB

# Import libraries to print as PDF
# #import dash_daq as daq
# #import weasyprint
# from dash import DashRenderer
# from weasyprint import HTML



# 1 ####### Load the GDP (current US$) data  ############################################################
gdp_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'gdp' / 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5728855' / 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5728855.csv'
# Reading csv file
df_gdp = pd.read_csv(gdp_file_path, skiprows=3)
# Filter the data to only include "Mozambique" row
mozambique_data = df_gdp[df_gdp['Country Name'] == 'Mozambique']
# Extract the years and GDP values from the dataframe
years_gdp = list(mozambique_data.columns[34:])
gdp_values = list(mozambique_data.values[0][34:])
# 1 ###### END Load the GDP (current US$) data  ############################################################

# 2 ####### Load the Debt data  ##################################################
# Load debt data from the CSV file
# Get the path to the 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5728786' directory relative to the current script's location
debt_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'debt' / 'API_GC.DOD.TOTL.GD.ZS_DS2_en_csv_v2_5872587.csv'
# Reading csv file
df_debt = pd.read_csv(debt_file_path, skiprows=3)
# Filter the data to only include "Mozambique" row
mozambique_data = df_debt[df_debt['Country Name'] == 'Mozambique']
# Extract the years and GDP values from the dataframe
years_debt = list(mozambique_data.columns[59:])
debt_values = list(mozambique_data.values[0][59:])
# 2 ###### END Load the debt data  ##################################################

# 2 ####### Load the natural resources data  ##################################################
# Load nr data from the CSV file
# Get the path to the directory relative to the current script's location
rl_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'naturalResources' / 'natResourcesRent_pct_GDP.csv'
# Reading csv file
df_nrList = pd.read_csv(rl_file_path, skiprows=0)

# 2 ####### Load the redList data  ##################################################
# Load rl data from the CSV file
# Get the path to the directory relative to the current script's location
rl_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'redListIndex' / 'red-list-index.csv'
# Reading csv file
df_redList = pd.read_csv(rl_file_path, skiprows=0)
# Filter the data to only include "Mozambique" row 
rl_mozambique_data = df_redList[df_redList['Country'] == 'Mozambique']
# Extract the years and RL values from the dataframe
years_rl = rl_mozambique_data['Year'].tolist(),
rl_values = rl_mozambique_data['15.5.1 - Red List Index - ER_RSK_LST'].tolist(),
# 2 ###### END Load the RedList data  ##################################################

# 2 ####### Load the GDP per capita (current US$) data  ##################################################
# Load GDP data from the CSV file
# Get the path to the 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5728786' directory relative to the current script's location
gdp2_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'gdp' / 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5728786' / 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5728786.csv'
# Reading csv file
df_gdp2 = pd.read_csv(gdp2_file_path, skiprows=3)
# Filter the data to only include "Mozambique" row
mozambique_data = df_gdp2[df_gdp2['Country Name'] == 'Mozambique']
# Extract the years and GDP values from the dataframe
years_gdp2 = list(mozambique_data.columns[34:])
gdp2_values = list(mozambique_data.values[0][34:])
# 2 ###### END Load the GDP per capita (current US$) data  ##################################################

# 3 ###### Load GDP growth (annual %) ####################################################
# Load GDP data from the CSV file
# Get the path to the 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5728786' directory relative to the current script's location
gdp3_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'gdp' / 'API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5728939' / 'API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5728939.csv'
# Reading csv file
df_gdp3 = pd.read_csv(gdp3_file_path, skiprows=3)
# Filter the data to only include "Mozambique" row
mozambique_data = df_gdp3[df_gdp3['Country Name'] == 'Mozambique']
# Extract the years and GDP values from the dataframe
years_gdp3 = list(mozambique_data.columns[24:])
gdp3_values = list(mozambique_data.values[0][24:])
# 3 ###### END Load GDP growth (annual %) ####################################################

# 4 ###### Inflation, Consumer Prices ####################################################
# Load inflation data from the CSV file
# Get the path to the file directory relative to the current script's location
inflation_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'cpi' / 'API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_5728859.csv'
# Reading csv file
df_inflation = pd.read_csv(inflation_file_path, skiprows=3)
# Filter the data to only include "Mozambique" row
mozambique_data = df_inflation[df_inflation['Country Name'] == 'Mozambique']
# Extract the years and inflation values from the dataframe
years_inflation = list(mozambique_data.columns[49:])
inflation_values = list(mozambique_data.values[0][49:])
# 4 ###### Inflation, Consumer Prices ####################################################

# 5 ###### START Load youth unemployment ####################################################
# Load youth unemployment data from the CSV file
# Get the path to the 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5728786' directory relative to the current script's location
yunemployment_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'unemployed_youth' / 'API_SL.UEM.1524.ZS_DS2_en_csv_v2_5729128' / 'API_SL.UEM.1524.ZS_DS2_en_csv_v2_5729128.csv'
# Reading csv file
df_yunemployment = pd.read_csv(yunemployment_file_path, skiprows=3)
# Filter the data to only include "Mozambique" row
mozambique_data = df_yunemployment[df_yunemployment['Country Name'] == 'Mozambique']
# Extract the years and youth unemployment values from the dataframe
years_yunemployment = list(mozambique_data.columns[34:])
yunemployment_values = list(mozambique_data.values[0][34:])
# 5 ###### END Load youth unemployment ####################################################

# 6 ###### START Consumer Price Index (CPI) #####################################################
# commented by rj cpi = pd.read_json(DATA_PATH.joinpath("mozambique_acute_food_insecurity_november_2022.json")) #
# Get the path to the 'data' directory relative to the current script's location
cpi_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'cpi' / 'cpi.json'
# Open the GeoJSON data
with open(cpi_file_path) as f:
    data_cpi = json.load(f)

# Extract data
xAxisLabels = data_cpi['xAxisLabels']
firstYAxis = data_cpi['firstYAxis']['values']
secondYAxis = data_cpi['secondYAxis']['values']

# # Flatten the nested structure in the JSON data using json_normalize
# #df_cpi = pd.json_normalize(data_cpi)
# # Extract the 'data' part of the JSON
# data_x = data_cpi['xAxisLabels']

# # Create a DataFrame from the flattened data
# xAxisLabels = pd.DataFrame(data_x)

# # Display the resulting DataFrame
# #print(xAxisLabels)

# #######
# # Extract the 'data' part of the JSON
# data_y1 = data_cpi['firstYAxis']
# data_y1 = data_y1['values']
# firstYAxis = pd.DataFrame(data_y1)

# # Display the resulting DataFrame
# #print(firstYAxis)


# #######
# # Extract the 'data' part of the JSON
# data_y2 = data_cpi['secondYAxis']
# data_y2 = data_y2['values']
# secondYAxis = pd.DataFrame(data_y2)

# # Display the resulting DataFrame
# #print(secondYAxis)

# 6 ###### END Consumer Price Index (CPI) ####################################################


#  ####### Load the GeoJSON data for FOOD INSECURITY #####################################

# Replace 'your_file_path.json' with the actual file path of your JSON file.
#file_path = r'Z:\Private\miguel.bambo\datascience\Dash\mais\data\1.economic\food_insecurity\Mozambique-Acute Food Insecurity November 2022.json'

# Get the path to the 'data' directory relative to the current script's location
gdf_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'food_insecurity' / 'Mozambique-Acute Food Insecurity November 2022.json'

# Open the GeoJSON data
with open(gdf_file_path) as f:
    data = json.load(f)

# Convert the GeoJSON data to a GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(data['features'])


# Define custom colors and text labels for each phase
phase_colors = {
    0: 'white',
    1: '#fee8c8',
    2: '#fc8d59',
    3: '#d7301f',
    4: '#7f0000',
    5: 'black'
}

phase_labels = {
    0: '0-Not Analyzed',
    1: '1-Minimal',
    2: '2-Stressed',
    3: '3-Crisis',
    4: '4-Emergency',
    5: '5-Famine'
}

# Map the phase values to colors and text labels in the GeoDataFrame
gdf['color'] = gdf['overall_phase_C'].map(phase_colors)
gdf['phase_label'] = gdf['overall_phase_C'].map(phase_labels)


######## END Load the GeoJSON data for FOOD INSECURITY ############################################


# Create a new instance of the Dash app for the Economic page
app = dash.Dash(__name__)

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
           

            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Summary"),
                                    html.Br([]),
                                    html.P(
                                    "Mozambique faces multiple contextual factors that could be “game changers”.\
                                    Each has the potential to affect the CDCS in significantly positive or \
                                    negative ways.  As a result, the Mission started the intervention named \
                                    Mozambique Adaption Information System (MAIS) in 2021 with support from \
                                    the Mozambique Monitoring, Evaluation Mechanism and Services (MMEMS), to \
                                    identify an approach that must support effective context monitoring and \
                                    inform adaptive decision-making in a rapidly evolving environment. \
                                    MAIS is meant to be a practical and sustainable system over time."\
                                    "The MAIS system is an innovative initiative that aims to provide \
                                    USAID/Mozambique with a platform for data visualization and analysis for \
                                    USAID/Mozambique’s development programs. However, the system was never \
                                    fully implemented due to various challenges and constraints. Currently, \
                                    USAID decided to reactivate the system with the support of MozMEL.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),

                    html.H6("List of Economic Indicators", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]),
                    html.P(html.A("Levels and location of food insecurity", href='#food-insecurity', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Fragile States Index", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Gross Domestic Product (GDP) and GDP growth rate", href='#row2', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Inflation rate", href='#row3', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Youth Unemployment rate", href='#row4', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Poverty rate and income distribution/Gini Index", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Foreign direct investment (FDI) inflows", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Trade balance and export/import levels", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Government debt and fiscal deficit", href='#row5', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Red List Index", href='#row5', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Natural Resources revenues", href='#row4', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Poverty rate and income", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Consumer Price Index (CPI)", href='#cpi', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"})),
                    html.P(html.A("Government revenues", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Government expenditure", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Debt servicing", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Exchange rate", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Net international reserves", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Interest rates/ MIMO rate", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("Employment and unemployment rate", style={"font-size": "10px", "color": "#888"})),
                    html.P(html.A("The ability of the country/economy to create jobs", style={"font-size": "10px", "color": "#888"})),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin                   

                    html.Br([]),html.Br([]),
                    html.H6("Annually Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin

                    #####
                    #####    
                    html.Div(
                        [
                            html.Div(
                                [   # Food Insecurity: October 2022 - March 2023 ##################
                                    html.H6("Food Insecurity: October 2022 - March 2023", className="subtitle padded"),
                                    dcc.Graph(
                                        id="choropleth-map", # Assign a unique id to the graph
                                        figure=update_map(None),  # Call the update_map function to initialize the map
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                        #style={"height": "450px", "margin-bottom": "0px"}  # Set/Adjust the height and margin-bottom of the choropleth map as needed  
                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: Integrated Food Security Phase Classification. Last Updated Date: March, 28th 2023.", href='https://www.ipcinfo.org/ipc-country-analysis/details-map/en/c/1155848/?iso3=MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})
                                            ]),
                                ],
                                className="twelve columns",
                                #style={"margin-bottom": "10px"}  # Adjust the margin-bottom to reduce the empty space
                                ),
                        ],
                        className="row ",
                        id = "food-insecurity",
                    ),
                    # Row 2
                    html.Div(
                        [   ##### GDP (current US$) #######
                            html.Div(
                                [
                                    html.H6(
                                        "GDP (current US$)",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        # figure=update_graph_2(),  # Call the update_graph_2 function to initialize the linechart/scatter plot
                                        figure={
                                             "data": [
                                                 go.Scatter(
                                                    x=years_gdp,
                                                    y=gdp_values,
                                                    mode='lines',
                                                    marker=dict(size=8),
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",
                                                 )
                                             ],
                                             "layout": go.Layout(
                                                 autosize=True,
                                        #         title="",
                                                 font={"family": "Raleway", "size": 10},
                                                 height=200,
                                                 width=340,
                                                 hovermode="closest",
                                        #         legend={
                                        #             "x": -0.0277108433735,
                                        #             "y": -0.142606516291,
                                        #             "orientation": "h",
                                        #         },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 20,
                                                },
                                        #         showlegend=True,
                                        
                                             ),
                                         },
                                         config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: The World Bank. Last Updated Date: July, 25th 2023.", href='https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=MZ', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
                                ],
                                className="six columns",
                            ),                     
                            html.Div(
                                [   ##### GDP per capita (current US$) #######
                                    html.H6(
                                        "GDP per capita (current US$)",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-3",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=years_gdp2,
                                                    y=gdp2_values,
                                                    mode='lines',
                                                    marker=dict(size=8),
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",                                                   
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                # legend={
                                                #     "x": -0.0228945952895,
                                                #     "y": -0.189563896463,
                                                #     "orientation": "h",
                                                #     "yanchor": "top",
                                                # },
                                                margin={
                                                    "r": 10,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 20,
                                                },
                                                #showlegend=True,
                                                title="",
                                             
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: The World Bank. Last Updated Date: July, 25th 2023.", href='https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?locations=MZ', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        id = "row2",
                    ),                   
                    # Row 3
                    html.Div(
                        [   ###### GDP growth (annual %) ###########
                            html.Div(
                                [
                                    html.H6(
                                        "GDP growth (annual %)", 
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=years_gdp3,
                                                    y=gdp3_values,
                                                    mode='lines',
                                                    marker=dict(size=8),
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",                                                   
                                                ),
                                            ],
                                         "layout": go.Layout(
                                                autosize=True,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                # legend={
                                                #     "x": -0.0228945952895,
                                                #     "y": -0.189563896463,
                                                #     "orientation": "h",
                                                #     "yanchor": "top",
                                                # },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 20,
                                                },
                                                #showlegend=True,
                                                title="",
                                             
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo

                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: The World Bank. Last Updated Date: July, 25th 2023.", href='https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=MZ', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
                                ],
                                className="six columns",
                            ),
                           
                            ###### Inflation, Consumer Prices (annual %) ###########
                           html.Div(
                                [
                                    html.H6(
                                        "Inflation, Consumer Prices (annual %)", 
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-5",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=years_inflation,
                                                    y=inflation_values,
                                                    mode='lines',
                                                    marker=dict(size=8),
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",                                                   
                                                ),
                                            ],
                                         "layout": go.Layout(
                                                autosize=True,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                # legend={
                                                #     "x": -0.0228945952895,
                                                #     "y": -0.189563896463,
                                                #     "orientation": "h",
                                                #     "yanchor": "top",
                                                # },
                                                margin={
                                                    "r": 10,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 10,
                                                },
                                                #showlegend=True,
                                                title="",
                                             
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: The World Bank. Last Updated Date: July, 25th 2023.", href='https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=MZ', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
                                ],
                                className="six columns",
                            ),                    
                        ],
                        className="row",
                        id = "row3",
                    ), ######### Closing DIV ######### 

                    # Row 4
                    html.Div(
                        [   ###### Youth Unemployment ###########
                            html.Div(
                                [
                                    html.H6(
                                        "Youth Unemployment (% of total labor force ages 15 - 24, modeled ILO estimate)", 
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-6",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=years_yunemployment,
                                                    y=yunemployment_values,
                                                    mode='lines',
                                                    marker=dict(size=8),
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",                                                   
                                                ),
                                            ],
                                         "layout": go.Layout(
                                                autosize=True,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                # legend={
                                                #     "x": -0.0228945952895,
                                                #     "y": -0.189563896463,
                                                #     "orientation": "h",
                                                #     "yanchor": "top",
                                                # },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 20,
                                                },
                                                #showlegend=True,
                                                title="",
                                             
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo

                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: The World Bank. Last Updated Date: September, 5th 2023.", href='https://data.worldbank.org/indicator/SL.UEM.1524.ZS?locations=MZ&most_recent_value_desc=false', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
                                ],
                                className="six columns",
                            ),

                            ###### Total Natural Resources Rents: % of GDP ###########
                            html.Div(
                                [
                                    html.H6("Total Natural Resources Rents: % of GDP", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-8",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_nrList['Year'],
                                                    y=df_nrList['Data'],
                                                    mode='lines',
                                                    marker=dict(size=8),
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",                                                   
                                                ),
                                            ],
                                         "layout": go.Layout(
                                                autosize=True,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                # legend={
                                                #     "x": -0.0228945952895,
                                                #     "y": -0.189563896463,
                                                #     "orientation": "h",
                                                #     "yanchor": "top",
                                                # },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 20,
                                                },
                                                #showlegend=True,
                                                title="",
                                             
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo

                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: CEIC. Last Updated Date: 2016", href='https://www.ceicdata.com/en/mozambique/land-use-protected-areas-and-national-wealth/mz-total-natural-resources-rents--of-gdp', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "20px"},
                        id = "row4",
                    ), ######### Closing DIV ######### 

                    ## Row5 ##
                    html.Div(
                        [   ###### Central Govenment debt, total (% of GDP) ###########
                            html.Div(
                                [
                                    html.H6("Central government debt, total (% of GDP) - Mozambique", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-8",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=years_debt,
                                                    y=debt_values,
                                                    mode='lines',
                                                    marker=dict(size=8),
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",                                                   
                                                ),
                                            ],
                                         "layout": go.Layout(
                                                autosize=True,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                # legend={
                                                #     "x": -0.0228945952895,
                                                #     "y": -0.189563896463,
                                                #     "orientation": "h",
                                                #     "yanchor": "top",
                                                # },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 20,
                                                },
                                                #showlegend=True,
                                                title="",
                                             
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo

                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: The World Bank. Last Updated Date: 2021.", href='https://data.worldbank.org/indicator/GC.DOD.TOTL.GD.ZS?end=2021&locations=MZ&start=2016&view=chart', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
                                ],
                                className="six columns",
                            ),
                           
                            ###### Red List Index ###########
                            html.Div(
                                [
                                    html.H6("Red List Index", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-CPI",
                                        figure={
                                            "data": [
                                                # go.Bar(
                                                #     x=xAxisLabels,
                                                #     y=secondYAxis,
                                                #     marker={
                                                #         "color": "#97151c",
                                                #         # "line": {
                                                #         #     "color": "rgb(255, 255, 255)",
                                                #         #     "width": 2,
                                                #         # },
                                                #     },
                                                #     name="Consumer Price Index",
                                                # ),
                                                go.Scatter(
                                                    x=rl_mozambique_data['Year'],
                                                    y=rl_mozambique_data['15.5.1 - Red List Index - ER_RSK_LST'],
                                                    mode='lines+markers',
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="% Change",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                #bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=250,
                                                hovermode="closest",
                                                # legend={
                                                #     "x": -0.0228945952895,
                                                #     "y": -0.189563896463,
                                                #     "orientation": "h",
                                                #     "yanchor": "top",
                                                # },
                                                margin={
                                                    "r": 10,
                                                    "t": 20,
                                                    "b": 30,
                                                    "l": 20,
                                                },
                                                showlegend=False,
                                                title="",
                                                width=330,
                                                # xaxis_title='Date',
                                                # yaxis_title='Value',
                                                
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": False,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": False,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: Red List Index, 1993 to 2022 (ourworldindata.org)", href='https://ourworldindata.org/grapher/red-list-index?tab=chart&country=~MOZ', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
        
                                ],

                                className="six columns",
                            ),                            
                        ],
                        className="row ",
                        id = "row5",
                    ), ######### Closing DIV ######### 

                    #####
                    # html.H6("Quarterly Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                    # html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin

                    html.H6("Montly Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin

                    html.Div(
                        [   
                             ###### Chart Consumer Price Index ###########
                            html.Div(
                                [
                                    html.H6(
                                        "Consumer Price Index (CPI)                           ",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-CPI",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=xAxisLabels,
                                                    y=secondYAxis,
                                                    marker={
                                                        "color": "#bbbbbb",
                                                        
                                                        # "line": {
                                                        #     "color": "rgb(255, 255, 255)",
                                                        #     "width": 2,
                                                        # },
                                                    },
                                                    name="% Change",
                                                    yaxis="y2",
                                                ),
                                                go.Scatter(
                                                    x=xAxisLabels,
                                                    y=firstYAxis,
                                                    mode='lines+markers',
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="CPI",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                #bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=250,
                                                width=340,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0428945952895,
                                                    "y": -0.209563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 20,
                                                    "t": 15,
                                                    "b": 20,
                                                    "l": 20,
                                                },
                                                showlegend=True,
                                                title="",
                                                # xaxis_title='Date',
                                                # yaxis_title='Value',
                                                
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": False,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "range": [220, 245],
                                                    "showgrid": True,
                                                    "showline": False,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "overlaying": "y2",
                                                },
                                                yaxis2={
                                                    "autorange": False,
                                                    "range": [-2, 3],
                                                    "showgrid": False,
                                                    "showline": False,
                                                    "title": "",
                                                    "side": "right",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                            
                                        },
                                        
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                    ),
                                    html.P([
                                            html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                            html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                            html.A("Source: International Monetary Fund (IMF). Last Updated Date: August, 31st 2023.", href='https://www.economy.com/mozambique/consumer-price-index-cpi', target="_blank", style={"font-size": "10px", "color": "#888"})
                                    ]),
        
                                ],
                                className="six columns",
                                id = "cpi",
                            ),
                        ],
                        className = "row ",
                    ),
                ],
                className="sub_page",                
            ),
        ],
        className="page",
        id = "top",
    )


################################################################################
###### UPDATING CHOROPLETH MAP GeoJSON data for FOOD INSECURITY ################
################################################################################

# Define the callback for the Choropleth Map
@app.callback(
    Output('choropleth-map', 'figure'),
    Input('choropleth-map', 'clickData')
)

######S#######
##############

def update_map(clickData):
    fig = go.Figure()

    for phase, color in phase_colors.items():
        phase_data = gdf[gdf['overall_phase_C'] == phase]
        # Convert GeoDataFrame to GeoJSON format
        geojson_data = phase_data.__geo_interface__
        fig.add_trace(go.Choroplethmapbox(
            geojson=geojson_data,
            locations=phase_data.index,
            z=phase_data['overall_phase_C'],
            colorscale=[[0, color], [1, color]],
            marker_opacity=0.7,
            marker_line_width=0,
            colorbar_title='Area Phase',
            name=phase_labels[phase],
            showscale=False
        ))



    fig.update_layout(mapbox_style="carto-positron", #The valid options for mapbox_style are: "open-street-map", "white-bg", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner", and "stamen-watercolor"
                        mapbox_zoom=3.5,
                        mapbox_center={"lat": -18.665695, "lon": 35.529562},
                        mapbox_layers=[]  # Hide default base map layers
                        )

# Add legend using annotations with a gray background
    legend_text = "<br>".join([f"<b><span style='color:{phase_colors[phase]}'>{phase_labels[phase]}</span></b>" for phase in phase_colors.keys()])
    fig.add_annotation(go.layout.Annotation(
        x=1.01,
        y=0.5,
        xanchor='left',
        yanchor='middle',
        text=legend_text,
        showarrow=False,
        font=dict(color='black', size=12),
        bgcolor='#cccccc',  # Add a gray background
        bordercolor='gray',
        borderwidth=0.05,
        align='left',
        # missing_kwds={
        # "color": "lightgrey",
        # "edgecolor": "red",
        # "hatch": "///",
        # "label": "Missing values",
        # }
        #margin=dict(r=0, #t=20, b=0
                    #)
        ))

    fig.update_layout(margin=dict(l=0, r=120, t=20, b=0))  # Adjust the right margin to accommodate the legend
    return fig

# Customize the layout of the bar 
#graph_CPI.update_layout(     title='Bar Chart',     xaxis_title='Date',     yaxis_title='Value',     showlegend=True) 

 

# Customize the layout of the line 
#chartline_chart.update_layout(     title='Line Chart',     xaxis_title='Date',     yaxis_title='Value',     showlegend=True)


    # START Putting Printing button as PDF
    # # Access the rendered HTML
    # rendered_html = DashRenderer(requests_pathname='/', requests_params='').response()

    # # Convert the rendered HTML to PDF
    # pdf = HTML(string=rendered_html.content).write_pdf("output.pdf")
    # END Putting Printing button as PDF


    ### START Show missing Data ##################################
    #     # Convert the GeoDataFrame to GeoDataFrame
    # gdf['color'] = gdf['overall_phase_C'].map(phase_colors)

    # # Plot the GeoDataFrame with assigned colors
    # ax = gdf.plot(column='color', figsize=(20, 20), missing_kwds={
    #     "color": "lightgrey",
    #     "edgecolor": "red",
    #     "hatch": "///",
    #     "label": "Missing values",
    # })
    # ax.axis('off')
    # #plt.show()
    ### END Show missing Data ##################################
    
        #return fig

###### UPDATING MAPS ####################################################################

#########################################################################################
###### ENDING UPDATING CHOROPLETH MAP GeoJSON data for FOOD INSECURITY ###################################################
#########################################################################################

#########################################################################################
###### UPDATING GDP (current US$) MAP ###################################################
#########################################################################################

# # Define the callback for the Graph-2 ScatterPlot CHART
# @app.callback(
#     Output('graph-2', 'figure'),
#     #Input('graph-2', 'clickData')
# )

# # Function to update graph-2 with GDP data
# def update_graph_2():



#     fig = go.Figure()
    
#     fig.add_trace(go.Scatter(
#         x=years,
#         y=gdp_values,
#         line={"color": "#97151c"},
#         mode="lines",
#         name="GDP (current US$)",
#         # x=years,
#         # y=gdp_values,
#         # line={"color": "#97151c"},
#         # mode="lines",
#         # name="GDP (current US$)",
#     ))
    
#     fig.update_layout(
#         autosize=True,
#         title="",
#         font={"family": "Raleway", "size": 10},
#         height=200,
#         width=340,
#         hovermode="closest",
#         legend={
#             "x": -0.0277108433735,
#             "y": -0.142606516291,
#             "orientation": "h",
#         },
#         margin={
#             "r": 20,
#             "t": 20,
#             "b": 20,
#             "l": 50,
#         },
#         showlegend=True,
#         xaxis={
#             "autorange": True,
#             "linecolor": "rgb(0, 0, 0)",
#             "linewidth": 1,
#             "showgrid": False,
#             "showline": True,
#             "title": "",
#             "type": "linear",
#         },
#         yaxis={
#             "autorange": False,
#             "gridcolor": "rgba(127, 127, 127, 0.2)",
#             "mirror": False,
#             "nticks": 4,
#             "showgrid": True,
#             "showline": True,
#             "ticklen": 10,
#             "ticks": "outside",
#             "title": "GDP (current US$)",
#             "type": "linear",
#             "zeroline": False,
#             "zerolinewidth": 4,
#         },
#         # autosize=True,
#         # title="",
#         # font={"family": "Raleway", "size": 10},
#         # height=200,
#         # width=340,
#         # hovermode="closest",
#         # legend={
#         #     "x": -0.0277108433735,
#         #     "y": -0.142606516291,
#         #     "orientation": "h",
#         # },
#         # margin={
#         #     "r": 20,
#         #     "t": 20,
#         #     "b": 20,
#         #     "l": 50,
#         # },
#         # showlegend=True,
#         # xaxis={
#         #     "autorange": True,
#         #     "linecolor": "rgb(0, 0, 0)",
#         #     "linewidth": 1,
#         #     #"range": [df_gdp['Year'].min(), df_gdp['Year'].max()],
#         #     "showgrid": False,
#         #     "showline": True,
#         #     "title": "",
#         #     "type": "linear",
#         # },
#         # yaxis={
#         #     "autorange": False,
#         #     "gridcolor": "rgba(127, 127, 127, 0.2)",
#         #     "mirror": False,
#         #     "nticks": 4,
#         #     #"range": [0, df_gdp['GDP (current US$)'].max() * 1.1],  # Adjust the range to have some margin at the top
#         #     "showgrid": True,
#         #     "showline": True,
#         #     "ticklen": 10,
#         #     "ticks": "outside",
#         #     "title": "GDP (current US$)",
#         #     "type": "linear",
#         #     "zeroline": False,
#         #     "zerolinewidth": 4,
#         # },
#     )
    
#     return fig

#########################################################################################
###### ENDING UPDATING GDP (current US$) MAP ############################################
#########################################################################################