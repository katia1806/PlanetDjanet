# Installed imports
import pandas as pd

# Internal imports
from src.mongodb_connection import MongoDBConnection


def transform_insta_publis():
    """Transform the Instagram publications data."""
    # initialization
    mongodb_connection = MongoDBConnection()
    
    # get the data from MongoDB
    df_all_content = pd.DataFrame(mongodb_connection.get_collection("all_content"))
    
    # close the MongoDB connection
    mongodb_connection.close()
    
    # filter the data
    df_insta_publis = df_all_content[df_all_content["Type de contenu"] == "Publication Instagram"][[
    "Mentions J’aime et réactions", "Commentaires", "Partages"]].reset_index()
    df_insta_publis.drop("index", axis=1)
    
    return df_insta_publis

def transform_facebook_publis():
    """Transform the Facebook publications data."""
    # initialization
    mongodb_connection = MongoDBConnection()
    
    # get the data from MongoDB
    df_all_content = pd.DataFrame(mongodb_connection.get_collection("all_content"))
    
    # close the MongoDB connection
    mongodb_connection.close()
    
    # filter the data
    df_fb_publis = df_all_content[df_all_content["Type de contenu"] == "Publication Facebook"][[
    "Mentions J’aime et réactions", "Commentaires", "Partages"]].reset_index()
    df_fb_publis.drop("index", axis=1)
    
    return df_fb_publis