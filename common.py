
# Standard library imports
import time
from datetime import datetime, date

# Intalled packages
import pandas as pd
import streamlit as st
from PIL import Image

def display_social_media_links():
    """Display social media links in the sidebar."""
    st.sidebar.markdown("#### Social Media Links")
    
    # Instagram Link
    st.sidebar.markdown(
        """<a href="https://www.instagram.com/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)
    
    # Facebook Link
    st.sidebar.markdown(
        """<a href="https://www.facebook.com/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/facebook-new.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)
    
    # Twitter Link
    st.sidebar.markdown(
        """<a href="https://twitter.com/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/twitter.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)
    
     # LinkedIn Link
    st.sidebar.markdown(
        """<a href="https://www.linkedin.com/in/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)



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
    ma_list = list(
        map(lambda x: float(x.replace(',', '.').replace('%', '')), ma_list))
    df.drop([column], axis=1)
    value = pd.DataFrame(ma_list).rename(columns={0: "Valeur"}, index={})
    return value
