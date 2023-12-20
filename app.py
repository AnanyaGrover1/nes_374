# Install packages if necessary
# !pip install streamlit plotly pandas geopandas numpy gspread google-auth statsmodels

# Import packages
import plotly.express as px
import pandas as pd
import geopandas as gpd
import numpy as np
import streamlit as st
import gspread
from google.auth import default
from oauth2client.client import GoogleCredentials

# Set up Google credentials
# creds, _ = default(scopes=['https://www.googleapis.com/auth/spreadsheets'])
# gc = gspread.authorize(creds)

# # Read data from Google Sheets into Pandas dataframe
# gsheet_url = 'https://docs.google.com/spreadsheets/d/14FwiUyhZhtpgNulfiM9P1HNJoa9Jy2MTlnEtOYiBAvU/edit?usp=sharing'
# sheet = gc.open_by_url(gsheet_url).sheet1
# rows = sheet.get_all_values()

df = pd.read_csv("data/GHDX_IPV.csv") # data on IPV
# df = pd.DataFrame.from_records(rows)
# new_header = df.iloc[0] # Grab the first row for the header
# df = df[1:] # Take the data less the header row
# df.columns = new_header # Set the header row as the df header

# Data pre-processing (same as the original code)
pct_changes = []
for country in df['Country'].unique():
  pct_changes.extend(df[df['Country']==country].iloc[:,2].astype(float).pct_change()*100)
df[f'Percent change in {df.iloc[:,2].name}'] = pct_changes

# read country coordinates
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.index = world['name']
world = world.reindex(df['Country'])
world['iso_a3'] = world['iso_a3'].fillna('NaN')
df['iso_a3'] = list(world['iso_a3'].reset_index(drop=True)) # drop country with no coordinates

# convert values to numbers
df[df.columns[1]] = df[df.columns[1]].astype(int) # year
df[df.columns[2]] = df[df.columns[2]].astype(float) # value
df[df.columns[3]] = df[df.columns[3]].astype(float) # percent change

# shorten column names
df = df.rename(columns={df.columns[2]:"Value of IPV metric over time",
                        df.columns[3]:"Percent change in IPV metric over time"})

# Page title
st.title("Visualizing Intimate Partner Violence in South West Asia and North Africa (SWANA)")

# Subtitle
data_description = "IPV Metric: Age-standardised prevalence of ever-partnered women aged 15 years and older who experienced physical or sexual violence by a current or former intimate partner in the last 12 months (%)"
st.write(data_description)

# Section 1: View data for all countries
st.header("View data for all countries")

# Get value for choropleth map
choropleth_value = st.selectbox(
    "Select the metric to display on the map:",
    df.columns[2:4],
    index=0
)

# Generate choropleth map
@st.cache_data
def create_choropleth(dataframe, value):
    # Function to plot IPV data on a choropleth map over a time series with color based on value
    fig = px.choropleth(dataframe,
                        locations='iso_a3',
                        color=value,
                        animation_frame='Year',
                        color_continuous_scale='thermal'  # Perceptually uniform and color-blind friendly
                        )
    fig.update_geos(fitbounds="locations", visible=True)
    fig.update_layout(title=value)
    fig.update_coloraxes(colorbar_title=value)
    return fig

choropleth_map = create_choropleth(df, choropleth_value)
st.plotly_chart(choropleth_map)

# Section 2: View data for one country
st.header("View data for one country")

# Get values for line graph
line_country = st.selectbox(
    "Select a country:",
    df['Country'].unique(),
    index=0
)
line_value = st.selectbox(
    "Select the metric for trendline:",
    df.columns[2:4],
    index=0
)

# Generate line graph
def update_graph(dataframe, country, value):
    dff = dataframe[dataframe['Country'] == country]
    fig = px.scatter(dff, y=value, x="Year", trendline="ols")  # Add Ordinary Least Squares regression line
    fig.update_layout(title=f"{value} for {country}")
    return fig

line_chart = update_graph(df, line_country, line_value)
st.plotly_chart(line_chart)

# Running Streamlit app
# Use the following command in the terminal to run the app:
# streamlit run your_script_name.py