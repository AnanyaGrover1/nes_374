import streamlit as st

st.set_page_config(page_title="Sources", page_icon="📊")

st.markdown("# 📊 Sources")
st.sidebar.header("Sources")


def main():
    st.markdown("""
        **Data sources:**
        - World bank gender statistics: [https://databank.worldbank.org/source/gender-statistics](https://databank.worldbank.org/source/gender-statistics#)
        - GHDX Intimate Partner Violence Data: [https://ghdx.healthdata.org/record/ihme-data/global-sustainable-development-goals-sdg-intimate-partner-violence-indicator-1990-2019](https://ghdx.healthdata.org/record/ihme-data/global-sustainable-development-goals-sdg-intimate-partner-violence-indicator-1990-2019)

        **Coding sources:**
        - Plotting package: Plotly [PyPlot](https://plotly.com/python/maps/)
        - Interactive Web App package: Streamlit [https://streamlit.io](https://streamlit.io)
        - [Introduction to Choropleth Maps and Time Series on Kaggle](https://www.kaggle.com/code/dabawse/introduction-to-choropleth-maps-and-time-series)
        - [Plotly Choropleth Maps](https://plotly.com/python/choropleth-maps/)
        - [Viridis Color Scale for Python](https://sjmgarnier.github.io/viridis/)
        - [Streamlit Deployment Documentation](https://docs.streamlit.io/en/stable/deploy_streamlit_app.html)
        - [Basic Callbacks with Streamlit](https://docs.streamlit.io/en/stable/api.html#callbacks)
        - [Example Streamlit App on GitHub](https://github.com/thusharabandara/dash-app-render-deployment)
    """)

if __name__ == "__main__":
    main()