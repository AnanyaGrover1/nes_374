# Import packages
import plotly.express as px
import pandas as pd
import geopandas as gpd
import streamlit as st
import textwrap

st.set_page_config(page_title="Visualizing IPV Risk Factors", page_icon="📈")

st.title("📈 Visualizing IPV Risk Factors")
st.sidebar.header("Visualizing IPV Risk Factors")

# Read data
context_df = pd.read_csv("data/worldbank_gender.csv")  # Data providing context to IPV

# DATA PRE-PROCESSING for context data (same as original code)
# separate the types of contextual data in other_df
# all data included are data that might inluence a woman's ability to escape intimate partner violence or become independent from her family
data_categories = {"Laws and legislations": [],
                   "Women's decision making freedom" : [],
                   "Women's beliefs" : [],
                   "Women's experiences" : []}
series_names = context_df["Series Name"].unique()
for name in series_names:
    if 'law' in name or 'legislation' in name or 'government' in name or 'A woman can' in name or 'A woman has' in name or 'rights' in name:
        data_categories["Laws and legislations"].append(name)
    elif 'decision' in name:
        data_categories["Women's decision making freedom"].append(name)
    elif 'believe' in name:
        data_categories["Women's beliefs"].append(name)
    elif 'experience' in name or 'behaviors' in name:
        data_categories["Women's experiences"].append(name)
    else:
        print(f"{name} is not categorized")

# reorganize the structure of other_df for ease of plotting
context_df = pd.wide_to_long(context_df, stubnames=["Y"], i=["Series Name", "Country Name"], j="Year")
context_df = context_df.reset_index()
context_df.columns = ['Series Name', 'Country', 'Year', 'Value over time']

# seperate the data for all the series
seperated_data = dict()
for series in context_df["Series Name"].unique():
    seperated_data[series] = context_df[context_df["Series Name"]==series].drop(labels=["Series Name"],axis=1)

# preprocess all series
for series in list(seperated_data.keys()):
    df = seperated_data[series]

    # Loop through each country to calculate the percent change in IPV value for more insights
    if not "(1=yes; 0=no)" in series:
        pct_changes = []
        for country in df['Country'].unique():
            pct_changes.extend(df[df['Country']==country].iloc[:,2].astype(float).pct_change()*100)
        df[f'Percent change in value over time'] = pct_changes

    # read country coordinates
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.index = world['name']
    world = world.reindex(df['Country'])
    world['iso_a3'] = world['iso_a3'].fillna('NaN')
    df['iso_a3'] = list(world['iso_a3'].reset_index(drop=True)) # drop country with no coordinates

    # convert values to the appropriate data type
    df["Year"] = df[df.columns[1]].astype(int) # year
    if "(1=yes; 0=no)" in series:
        df['Value over time'] = df[df.columns[2]].astype(bool) # value
    else:
        df['Value over time'] = df[df.columns[2]].astype(float) # value
        df['Percent change in Value over time'] = df[df.columns[3]].astype(float) # percent change


def choropleth(df, series, color_field, discrete_color_map=None):
    df = df.sort_values("Year")
    if discrete_color_map:
        fig = px.choropleth(df,
                            locations='iso_a3',
                            color=color_field,
                            animation_frame='Year',
                            color_discrete_map=discrete_color_map)
    else:
        fig = px.choropleth(df,
                            locations='iso_a3',
                            color=color_field,
                            animation_frame='Year',
                            color_continuous_scale='thermal')  # Perceptually uniform and color-blind friendly

    fig.update_geos(lataxis_range=[-5, 50],
                    lonaxis_range=[-20, 85],
                    visible=True)
    fig.update_layout(title=f"{'<br>'.join(textwrap.wrap(series, 98))}<br>{color_field}",
                      title_automargin=True, title_x=0.5, title_y=0.97, title_xanchor='center')

    if not discrete_color_map:
        fig.update_coloraxes(colorbar_title_text=color_field)

    return fig

# Prepare page
st.write("This page contains data on factors that are likely to affect a woman's family status and independence, as well as her opportunities to survive and/or escape a situation of domestic abuse.")

st.write("Note that some of this data is sparse, may have missing values, or is not available for all years, which will affect the visualizations.")

st.write("Over time, we can observe from the map that women now have greater rights in more countries, such as having the ability travel out of their homes in the same away as a man, not being legally bound to obey their husbands, and being able to be the head of the household, but other restrictions such as the ability to get a divorce remain the same.")

# Loop over all categories and data series
for category_name, series_list in data_categories.items():
    st.header(category_name)
    selected_series = st.selectbox(f"Select series for {category_name}:", series_list, key=f"{category_name}-series")
    df = seperated_data[selected_series]

    if "(1=yes; 0=no)" in selected_series:
        data_values = ["Value over time"]
        selected_data_value = st.selectbox("Select data value for choropleth map:", data_values, key=f"{category_name}-data-value")
        map_figure = choropleth(df, selected_series, selected_data_value, discrete_color_map={True: 'green', False: 'red'})
    else:
        data_values = ["Value over time", "Percent change in value over time"]
        selected_data_value = st.selectbox("Select data value for choropleth map:", data_values, key=f"{category_name}-data-value")
        map_figure = choropleth(df, selected_series, selected_data_value)

    st.plotly_chart(map_figure)

# To run this Streamlit app, run the following command in the terminal:
# streamlit run context.py