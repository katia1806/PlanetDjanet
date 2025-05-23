# meta.py
# Standard imports
import math


# Installed imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum

# Internal imports
from src.view.common import separate_percentage
from src.controllers.meta_controller import (
    get_metrics_data, 
    get_pub_data, 
    get_likes_gender_age_data,
    get_likes_city_data,
    get_couverture_data)


def display_metrics():
    """Display the metrics of the instagram and facebook
    Args:
        df_insta_publis: The instagram publications DataFrame.
        df_fb_publis: The facebook publications DataFrame.
    """
    # initialization
    df_insta_publis ,df_fb_publis = get_metrics_data()
    
    # calculate the number of likes, comments and shares
    num_like = df_insta_publis["Mentions J’aime et réactions"].sum(
    )+df_fb_publis["Mentions J’aime et réactions"].sum()
    num_comment = df_insta_publis["Commentaires"].sum(
    )+df_fb_publis["Commentaires"].sum()
    num_share = df_insta_publis["Partages"].sum(
    )+df_fb_publis["Partages"].sum()
    
    # title of the metrics
    st.markdown(
        "<h3 style='text-align: center;'>Metrics for Facebook and Instagram</h3>", unsafe_allow_html=True)
    # show the metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Likes", num_like)
    col2.metric("Comments", num_comment)
    col3.metric("Shares", num_share)


def display_advertisment_tendancy():
    """Display the advertisment tendancy"""
    # initialization
    df_pub = get_pub_data()
    colors = "red"
    area = 40 # the area of the points
    
    # initialize the graph
    fig, _ = plt.subplots()
    plt.scatter(df_pub["AD_ACCOUNT,SPEND,COUNT"], df_pub[
                'AD_ACCOUNT,IMPRESSION,UNIQUE_USERS'], area, colors, alpha=0.5)
    plt.ylim(0, 15000)
    plt.xlim(0, 1200)
    plt.xlabel("Amount spent on advertisments")
    plt.ylabel("Impressions by unique users")
    
    # display the advertisment tendancy graph
    st.markdown(
        "<h3 style='text-align: center;'>Advertisment Tendancy</h3>", unsafe_allow_html=True)
    st.pyplot(fig)

def display_likes_by_genders_and_ages():
    """Display the likes by gender and age
    """
    # initialization
    df_likes_gender_age = get_likes_gender_age_data()
    
    # get the percentage of women and men
    df_women_percentage, df_likes_gender_age = separate_percentage(
        df_likes_gender_age, "Femmes")
    df_men_percentage, df_likes_gender_age = separate_percentage(
        df_likes_gender_age, "Hommes")
    # assign the sexe column
    df_women_percentage = df_women_percentage.assign(Sexe="Femmes")
    df_men_percentage = df_men_percentage.assign(Sexe="Hommes")
    
    # concatenate the two DataFrames and reset the index
    df_genders_percentage = pd.concat([df_women_percentage, df_men_percentage], join="outer")
    df_genders_percentage = df_genders_percentage.reset_index().rename(
        columns={"index": "Age"}, index={})
    
    # initialize the graph
    fig, ax = plt.subplots()
    # set the x and y axis
    sns.barplot(x="Age", y="Valeur", hue="Sexe", data=df_genders_percentage)
    # set the x axis labels
    ax.set_xticklabels(
        ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"])
    # set the y axis labels
    ax.set_ylabel("Percentage of likes %")
    
    # display the representation of likes by gender and age graph
    st.markdown(
        "<h3 style='text-align: center;'>Representation of likes by gender and age</h3>", unsafe_allow_html=True)
    st.pyplot(fig)
    
def display_likes_by_cities():
    """Display the likes by city"""
    # initialization
    df_likes_city = get_likes_city_data()
    
    # separate the percentage
    value, df_likes_city = separate_percentage(df_likes_city, "Valeur")
    # calculate the angle
    df_likes_city['angle'] = value['Valeur'] / \
        value['Valeur'].sum() * 2*math.pi
    # set the color
    df_likes_city['color'] = Category20c[len(df_likes_city)]
    
    # initialize the graph
    p = figure(height=350, title="Pie Chart", toolbar_location=None,
                tools="hover", tooltips="@df_likes_city.Principales villes: @Valeur", x_range=(-0.5, 1.0))
    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='Principales villes', source=df_likes_city)
    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    
    # display the representation of the number of likes by cities graph   
    st.markdown(
        "<h3 style='text-align: center;'>Representation of the number of likes by cities</h3>", unsafe_allow_html=True) 
    st.bokeh_chart(p, use_container_width=True)
    

def display_distribution_fb_ins():
    """Display the distribution of the facebook and instagram"""
    # initialization
    df_couverture = get_couverture_data()
    
    # display the representation of the reach distribution facebook instagram
    st.markdown(
        "<h3 style='text-align: center;'>Comparaison of the reach destribution Facebook Instagram August/Sep</h3>", unsafe_allow_html=True) 
    st.markdown(
        "<h4>Representation 1:</h4>", unsafe_allow_html=True) 
    st.line_chart(df_couverture, x="Date", y=[
                    "Couverture Instagram", "Couverture de la Page Facebook"])
    st.markdown(
        "<h4>Representation 2:</h4>", unsafe_allow_html=True) 
    st.bar_chart(df_couverture, x="Date", y=[
                    "Couverture Instagram", "Couverture de la Page Facebook"], use_container_width=True)

    

def display():
    """Display the Meta page"""
    # title of the dashboard
    st.markdown(
        "<h2 style='text-align: center;'>Meta Dashboard</h2>", unsafe_allow_html=True)
    
    # initialize the containers
    metrics = st.container()
    advertisment_tendancy = st.container()
    likes_by_genders_and_ages = st.container()
    likes_by_cities = st.container()
    distribution_fb_ins = st.container()
    
    # meta metrics
    with metrics:
        display_metrics()
        
    # advertisment tendancy
    with advertisment_tendancy:
        display_advertisment_tendancy()
        
    # likes by gender and age
    with likes_by_genders_and_ages:
        display_likes_by_genders_and_ages()
    
    # likes by cities
    with likes_by_cities:
        display_likes_by_cities()
        
    # distribution facebook and instagram
    with distribution_fb_ins:
        display_distribution_fb_ins()