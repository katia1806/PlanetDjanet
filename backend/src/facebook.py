# facebook.py
import pandas as pd
import json
from datetime import datetime
from common import to_date, get_month, get_year, get_week, by_month, by_week

def load_facebook_data():
    """Load and preprocess Facebook data."""
    # Replace these file paths with the correct paths or database queries
    df_couverture_fb = pd.read_csv("Couverture.csv", delimiter=",",  engine='python', encoding= "UTF-16")
    df_likes_fb = pd.read_csv("Visits_Fb.csv", delimiter=",",  engine='python', encoding= "UTF-16")
    df_fb_publis = pd.read_csv("Tous les contenus.csv", delimiter=",",  engine='python', encoding= "UTF-8")
    df_fb_publis = df_fb_publis[df_fb_publis["Type de contenu"]=="Publication Facebook"][["Légende","Mentions J’aime et réactions","Commentaires","Partages","Clics sur le lien"]].reset_index(drop=True)

    # Process dates
    to_date(df_couverture_fb)
    to_date(df_likes_fb)
    to_date(df_fb_publis)

    return df_couverture_fb, df_likes_fb, df_fb_publis