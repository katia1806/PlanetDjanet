# facebook_page.py

import streamlit as st
import plotly.express as px

# Internal imports
from .common import by_month, by_week
import requests

BACKEND_URL = "http://backend:8000"


def display():
    response = requests.get(f"{BACKEND_URL}/facebook")    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to retrieve data: {response.status_code}")    
    if response.status_code == 200:  
        files = response.json()  
        df_fb_publis = files["df_fb_publis"]
        df_likes_fb = files["df_likes_fb"]
        df_couverture_fb = files["df_couverture_fb"]
        
        # Facebook Dashboard UI
        st.header("Facebook Dashboard")

        # Metrics
        st.subheader("Metrics")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Likes", df_fb_publis["Mentions J’aime et réactions"].sum())
        col2.metric("Comments", df_fb_publis["Commentaires"].sum())
        col3.metric("Shares", df_fb_publis["Partages"].sum())
        col4.metric("Link Clicks", df_fb_publis["Clics sur le lien"].sum())

        # Reach Representation
        col1, col2 = st.columns(2)
        col1.subheader("Representation of the reach August/Sep")
        col1.line_chart(df_couverture_fb["Couverture de la Page Facebook"])
        col2.bar_chart(df_couverture_fb["Couverture de la Page Facebook"])

        # New Likes Analysis
        st.subheader("Number of new likes")
        col1, col2 = st.columns(2)
        with col1:
            year = st.selectbox("Year", (2020, 2021, 2022))
        with col2:
            time_frame = st.selectbox(
                "Select weekly or monthly reaches", ("weekly", "monthly"))

        # Data Aggregation
        agg_func = by_week if time_frame == "weekly" else by_month
        selected_data_streamlit = agg_func(
            df_likes_fb, year, "Mentions J’aime de la Page Facebook")

        # Displaying Bar Chart
        fig3 = px.bar(selected_data_streamlit,
                    x=time_frame[:-2], y="Mentions J’aime de la Page Facebook")
        st.plotly_chart(fig3, use_container_width=True)

        # Publications with More Than 20 Comments
        st.subheader("The publications that got more than 20 comments")
        text = df_fb_publis[df_fb_publis["Commentaires"] > 20]["Légende"]
        st.write(text)
    else :
        st.error(f"Failed to retrieve data: {response.status_code}")
# This function should be called from the main app.py file when the Facebook page is selected
