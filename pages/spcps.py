#import dash_core_components as dcc #Deprecated
import dash
from dash import dcc
#import dash_html_components as html #Deprecated
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import geopandas as gpd
import json
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


# Get the path to the 'data' directory relative to the current script's location
gdf_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'food_insecurity' / 'Mozambique-Acute Food Insecurity November 2022.json'

# Open the GeoJSON data
with open(gdf_file_path) as f:
    data = json.load(f)

# Convert the GeoJSON data to a GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(data['features'])

#print(data);

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
app = dash.Dash(__name__)

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    html.H6("Objective 1: Resilient Civil Society", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]),
                    html.P("Number of people with acute food insecurity", style={"font-size": "10px", "color": "#888"}),
                    html.P("Freedom of press", style={"font-size": "10px", "color": "#888"}),
                    html.P("Political Rights", style={"font-size": "10px", "color": "#888"}),
                    html.P("Civil Liberties", style={"font-size": "10px", "color": "#888"}),
                    html.P("Electoral credibility", style={"font-size": "10px", "color": "#888"}),
                    html.P("Laws and GRM actions that impose restrictions or undermine civil society", style={"font-size": "10px", "color": "#888"}),
 
                    html.H6("Objective 2: Security, justice and human rights", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]),                    
                    html.P("Total number of political violence events", style={"font-size": "10px", "color": "#888"}),
                    html.P("Total number of reported fatalities from political violence", style={"font-size": "10px", "color": "#888"}),
                    html.P("Total number of reported fatalities from political violence targeting civilians", style={"font-size": "10px", "color": "#888"}),
                    html.P("Number of events of violence against civilians by state or state aligned actors", style={"font-size": "10px", "color": "#888"}),
                    html.P("Number of events of violence against civilians by insurgents/rebel groups", style={"font-size": "10px", "color": "#888"}),
                    html.P("Number of security incidents",  style={"font-size": "10px", "color": "#888"}),
                    html.P("Political Stability and Absence of Violence/Terrorism", style={"font-size": "10px", "color": "#888"}),
                    html.P("Rule of Law", style={"font-size": "10px", "color": "#888"}),
                    html.P("Control of Corruption", style={"font-size": "10px", "color": "#888"}),
                    html.P("Impartiality of the judicial system", style={"font-size": "10px", "color": "#888"}),
                    html.P("Absence of corruption in state institutions", style={"font-size": "10px", "color": "#888"}),
                    html.P("Equal political power", style={"font-size": "10px", "color": "#888"}),
                    html.P("Equal political representation", style={"font-size": "10px", "color": "#888"}),
                    html.P("Equal civil liberties", style={"font-size": "10px", "color": "#888", }),
                    html.P("Presence of foreign military forces", style={"font-size": "10px", "color": "#888", }),
 
                    html.H6("Objective 3: Inclusive, diversified economic growth", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]), 
                    html.P("LNG Investments (milestone based)", style={"font-size": "10px", "color": "#888"}),
                    html.P("Economic growth", style={"font-size": "10px", "color": "#888"}),
                    html.P("Exchange rate", style={"font-size": "10px", "color": "#888"}),
                    html.P("Average consumer price inflation", style={"font-size": "10px", "color": "#888"}),
                    html.P("Equal socioeconomic opportunity", style={"font-size": "10px", "color": "#888"}),
                    html.P("Employment in agriculture, industry, services (% total employment, disaggregated by male/female)",  style={"font-size": "10px", "color": "#888"}),
                    html.P("Unemployment, youth", style={"font-size": "10px", "color": "#888"}),
                    html.P("Export structure by group (food, fuels, minerals, etc)", style={"font-size": "10px", "color": "#888"}),
                    html.P("FDI Inflows (millions of USD)", style={"font-size": "10px", "color": "#888"}),

                    html.H6("Objective 4: Inclusive governance for service delivery", style={'margin-bottom': '0'}),
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]), 
                    html.P("Number of displaced people", style={"font-size": "10px", "color": "#888"}),
                    html.P("Returning IDPs", style={"font-size": "10px", "color": "#888"}),
                    html.P("Urgent needs of IDPs", style={"font-size": "10px", "color": "#888"}),
                    html.P("Demographic profile", style={"font-size": "10px", "color": "#888"}),
                    html.P("Equal access to public services", style={"font-size": "10px", "color": "#888"}),
                    html.P("Human Development Index",  style={"font-size": "10px", "color": "#888"}),
                    html.P("Humanitarian Response Trends:", style={"font-size": "10px", "color": "#888"}),
                    html.P(".    Number of people in northern Mozambique in need of life-saving and life-sustaining humanitarian assistance due to the impact of armed conflict, violence and insecurity in the region.", style={"font-size": "10px", "color": "#888"}),
                    html.P(".    Number of people reached with some form of humanitarian assistance versus number of people in need of HA", style={"font-size": "10px", "color": "#888"}),
                    html.P(".    Percent of Humanitarian Response Plan (HRP) in northern Mozambique funded ", style={"font-size": "10px", "color": "#888"}),


                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    html.Br([]),html.Br([]),                    
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
                        [
                            html.Div([
                                        html.H6("Graph 1", className="subtitle padded"),
                                        # dcc.Graph(
                                        #     id="graph-1",
                                        #     figure={
                                        #         "data": [
                                        #             go.Scatter(
                                        #                 x=years_mmr,
                                        #                 y=mmr_values,
                                        #                 line={"color": "#97151c"},
                                        #                 marker=dict(size=3),
                                        #                 mode="lines+markers",
                                        #                 name="",
                                        #             ),
                                        #         ],
                                        #         "layout": go.Layout(
                                        #             autosize=True,
                                        #              width=340,
                                        #              height=200,
                                        #             font={"family": "Raleway", "size": 10},
                                        #             margin={
                                        #                 "r": 30,
                                        #                 "t": 30,
                                        #                 "b": 30,
                                        #                 "l": 30,
                                        #             },
                                        #             showlegend=False,
                                        #             titlefont={
                                        #                 "family": "Raleway",
                                        #                 "size": 10,
                                        #             },
                                        #             xaxis={
                                        #                 "autorange": True,
                                        #                 "range": [
                                        #                     "2007-12-31",
                                        #                     "2018-03-06",
                                        #                 ],
                                        #                 "rangeselector": {
                                        #                     "buttons": [
                                        #                         {
                                        #                             "count": 5,
                                        #                             "label": "5Y",
                                        #                             "step": "year",
                                        #                             "stepmode": "backward",
                                        #                         },
                                        #                         {
                                        #                             "count": 10,
                                        #                             "label": "10Y",
                                        #                             "step": "year",
                                        #                             "stepmode": "backward",
                                        #                         },
                                        #                         {
                                        #                             "count": 15,
                                        #                             "label": "15Y",
                                        #                             "step": "year",
                                        #                         },
                                        #                         {
                                        #                             "count": 20,
                                        #                             "label": "20Y",
                                        #                             "step": "year",
                                        #                             "stepmode": "backward",
                                        #                         },
                                        #                         {
                                        #                             "label": "All",
                                        #                             "step": "all",
                                        #                         },
                                        #                     ]
                                        #                 },
                                        #                 "showline": False,
                                        #                 "type": "date",
                                        #                 "zeroline": False,
                                        #             },
                                        #             yaxis={
                                        #                 "autorange": True,
                                        #                 "range": [
                                        #                     18.6880162434,
                                        #                     278.431996757,
                                        #                 ],
                                        #                 "showline": False,
                                        #                 "type": "linear",
                                        #                 "zeroline": False,
                                        #             },
                                        #         ),
                                        #     },
                                        #     config={"displayModeBar": False},
                                        # ),
                                        # html.P([
                                        #         html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                        #         html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                        #         html.A("Source: World Bank", href='https://data.worldbank.org/indicator/SH.STA.MMRT?end=2020&locations=MZ&start=2000&view=chart', target="_blank", style={"font-size": "10px", "color": "#888"})
                                        #     ]),
                                        #html.P(),
                                        
                                ],
                                        className = "six columns",
                            ),
                            html.Div([  
                                        html.H6("Graph 2", className="subtitle padded"),
                                        # dcc.Graph(
                                        #     id="graph-2",
                                        #     figure={
                                        #         "data": [
                                        #             go.Bar(
                                        #                 x=years_litr,
                                        #                 y=litr_values,
                                        #                 marker={
                                        #                 "color": "#97151c",
                                        #                 },                                                        
                                        #                 # name="",
                                        #             ),
                                        #         ],
                                        #         "layout": go.Layout(
                                        #             autosize=True,
                                        #              width=340,
                                        #              height=200,
                                        #             font={"family": "Raleway", "size": 10},
                                        #             margin={
                                        #                 "r": 30,
                                        #                 "t": 30,
                                        #                 "b": 30,
                                        #                 "l": 30,
                                        #             },
                                        #             showlegend=False,
                                        #             titlefont={
                                        #                 "family": "Raleway",
                                        #                 "size": 10,
                                        #             },
                                        #             xaxis={
                                        #                 "autorange": True,
                                        #                 "range": [
                                        #                     "2007-12-31",
                                        #                     "2018-03-06",
                                        #                 ],
                                        #                 "rangeselector": {
                                        #                     "buttons": [
                                        #                         {
                                        #                             "count": 5,
                                        #                             "label": "5Y",
                                        #                             "step": "year",
                                        #                             "stepmode": "backward",
                                        #                         },
                                        #                         {
                                        #                             "count": 10,
                                        #                             "label": "10Y",
                                        #                             "step": "year",
                                        #                             "stepmode": "backward",
                                        #                         },
                                        #                         {
                                        #                             "count": 15,
                                        #                             "label": "15Y",
                                        #                             "step": "year",
                                        #                         },
                                        #                         {
                                        #                             "count": 20,
                                        #                             "label": "20Y",
                                        #                             "step": "year",
                                        #                             "stepmode": "backward",
                                        #                         },
                                        #                         {
                                        #                             "label": "All",
                                        #                             "step": "all",
                                        #                         },
                                        #                     ]
                                        #                 },
                                        #                 "showline": False,
                                        #                 "type": "date",
                                        #                 "zeroline": False,
                                        #             },
                                        #             yaxis={
                                        #                 "autorange": True,
                                        #                 "range": [
                                        #                     18.6880162434,
                                        #                     278.431996757,
                                        #                 ],
                                        #                 "showline": False,
                                        #                 "type": "linear",
                                        #                 "zeroline": True,
                                        #             },
                                        #         ),
                                        #     },
                                        #     config={"displayModeBar": False},
                                        # ),
                                        # html.P([
                                        #         html.A("Top", href='#top', style={"font-size": "10px", "color": "#888", "border-bottom": "1px solid #888"}),
                                        #         html.A(" | ", href='#top', style={"font-size": "10px", "color": "#888"}),
                                        #         html.A("Source: World Bank", href='https://data.worldbank.org/indicator/SE.ADT.LITR.ZS?end=2021&locations=MZ-ZA&name_desc=false&start=1980&view=chart', target="_blank", style={"font-size": "10px", "color": "#888"})
                                        #         ]),

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


# Define the callback for the Choropleth Map
@app.callback(
    Output('choropleth-map', 'figure'),
    Input('choropleth-map', 'clickData')
)


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

    fig.update_layout(
        mapbox_style="carto-positron", #The valid options for mapbox_style are: "open-street-map", "white-bg", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner", and "stamen-watercolor"
        mapbox_zoom=4.0,
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
        ))
    fig.update_layout(margin=dict(l=0, r=120, t=20, b=0))  # Adjust the right margin to accommodate the legend
    return fig