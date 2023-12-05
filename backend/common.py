# Standard library imports
from datetime import datetime, date
import json
import math
import time

# Related third party imports
from bokeh.layouts import gridplot
from bokeh.models import Panel, Tabs
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
import altair as alt
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff
import pydeck as pdk
import seaborn as sns
import streamlit as st
from tkinter import filedialog

def get_image(path: str) -> Image:
    """Load an image from the given path.
    
    Parameters:
    - path (str): Path of the image file.
    
    Returns:
    - Image: PIL Image object.
    """
    image = Image.open(path)
    return image

def to_date(X):
    """Convert the 'Date' column of a DataFrame to datetime format."""
    X['Date'] = pd.to_datetime(X['Date'], format='%Y-%m-%d %H:%M:%S')

def get_month(dt): 
    """Extract the month from a datetime object."""
    return dt.month

def get_year(dt): 
    """Extract the year from a datetime object."""
    return dt.year

def get_week(dt): 
    """Extract the week from a datetime object."""
    return dt.week

def by_month(data, year, column):
    """Aggregate data by month for a specific year."""
    agg_by_month = data[data["year"] == year].groupby("month")[column].sum()
    return pd.DataFrame(agg_by_month).reset_index()

def by_week(data, year, column):
    """Aggregate data by week for a specific year."""
    agg_by_week = data[data["year"] == year].groupby("week")[column].sum()
    return pd.DataFrame(agg_by_week).reset_index()

@st.cache()
def get_lat_long(x, processing_media_list=False):
    """Extract latitude and longitude from a JSON structure."""
    try:
        metadata = x["media"][0]["media_metadata"] if processing_media_list else x["media_map_data"]["Media Thumbnail"]["media_metadata"]
        exif_data = metadata["photo_metadata"]["exif_data"] if "photo_metadata" in metadata else metadata["video_metadata"]["exif_data"]
        return {'lat': exif_data[0]['latitude'], 'lon': exif_data[0]['longitude']}
    except:
        return None

@st.cache()
def get_accounts(x):
    """Extract account information from a JSON structure."""
    try:
        string_list_data = x["string_list_data"]
        return {'value': string_list_data[0]['value']}
    except:
        return None

@st.cache()
def delete_percentage(df, column):
    """Delete percentage signs from a column in a DataFrame."""
    time.sleep(1)    
    ma_list = list(df[column])
    ma_list = list(map(lambda x: float(x.replace(',', '.').replace('%', '')), ma_list))
    df.drop([column], axis=1)
    value = pd.DataFrame(ma_list).rename(columns={0: "Valeur"}, index={})
    return value
