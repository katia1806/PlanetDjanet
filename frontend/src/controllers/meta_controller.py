# Standard imports
import requests
import os

# Installed imports
import pandas as pd

# Constant
BACKEND_HOST = os.getenv('BACKEND_HOSTNAME', 'planet_djanet')

def get_metrics_data() -> (pd.DataFrame, pd.DataFrame):
    """Retrieve metrics data for meta page
    Returns:
        The metrics data.
    """
    # get the data from the backend
    response = requests.get(f"http://{BACKEND_HOST}:8000/meta/metrics")
    data = response.json()

    # separate the data
    insta_data = data['df_insta_publis']
    fb_data = data['df_fb_publis']

    # transform the data into DataFrame
    df_insta_publis = pd.read_json(insta_data,encoding="utf-8", orient='records')
    df_fb_publis = pd.read_json(fb_data,encoding="utf-8", orient='records')
    
    return df_insta_publis ,df_fb_publis

def get_pub_data() -> pd.DataFrame:
    """Retrieve pub data for meta page
    Returns:
        df_pub: The pub data.
    """
    # get the data from the backend
    response = requests.get(f"http://{BACKEND_HOST}:8000/meta/pub")
    data = response.json()

    # transform the data into DataFrame
    df_pub = pd.read_json(data,encoding="utf-8", orient='records')
    
    return df_pub

def get_likes_gender_age_data() -> pd.DataFrame:
    """Retrieve likes by gender and age data for meta page
    Returns:
        df_likes_gender_age: The likes by gender and age data.
    """
    # get the data from the backend
    response = requests.get(f"http://{BACKEND_HOST}:8000/meta/likes_gender_age")
    data = response.json()

    # transform the data into DataFrame
    df_likes_gender_age = pd.read_json(data,encoding="utf-8", orient='records')
    
    return df_likes_gender_age

def get_likes_city_data() -> pd.DataFrame:
    """Retrieve likes by city data for meta page
    Returns:
        df_likes_city: The likes by city data.
    """
    # get the data from the backend
    response = requests.get(f"http://{BACKEND_HOST}:8000/meta/likes_city")
    data = response.json()

    # transform the data into DataFrame
    df_likes_city = pd.read_json(data,encoding="utf-8", orient='records')
    
    return df_likes_city

def get_couverture_data() -> pd.DataFrame:
    """Retrieve couverture of facebook and instagram data for meta page
    Returns:
        df_couverture: The couverture of facebook and instagram data.
    """
    # get the data from the backend
    response = requests.get(f"http://{BACKEND_HOST}:8000/meta/couverture")
    data = response.json()

    # transform the data into DataFrame
    df_couverture = pd.read_json(data,encoding="utf-8", orient='records')
    
    return df_couverture