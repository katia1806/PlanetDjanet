# Installed imports
import pandas as pd

# Internal imports
from src.mongodb_connection import MongoDBConnection


def transform_insta_publis() -> pd.DataFrame:
    """Transform the Instagram publications data.
    Returns:
        The Instagram publications DataFrame.
    """
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

def transform_facebook_publis() -> pd.DataFrame:
    """Transform the Facebook publications data.
    Returns:
        The Facebook publications DataFrame.
    """
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

def transform_pub() -> pd.DataFrame:
    """Transform the advertisment data.
    Returns:
        The advertisment DataFrame.
    """
    # initialization
    mongodb_connection = MongoDBConnection()
    
    # get the data from MongoDB
    df_pub = pd.DataFrame(mongodb_connection.get_collection("pub"))
    # close the MongoDB connection
    mongodb_connection.close()
    
    # drop the date column
    df_pub = df_pub.drop("Date", axis=1)
    # get the top 10 advertisment tendancy
    df_pub["AD_ACCOUNT,IMPRESSION,UNIQUE_USERS"].nlargest(10)
    
    return df_pub

def transform_likes_gender_age() -> pd.DataFrame:
    """Transform the likes by gender and age data.
    Returns:
        The likes by gender and age DataFrame.
    """
    # initialization
    mongodb_connection = MongoDBConnection()
    
    # get the data from MongoDB
    df_likes_gender_age = pd.DataFrame(mongodb_connection.get_collection("likes_gender_age"))
    # close the MongoDB connection
    mongodb_connection.close()
    
    return df_likes_gender_age
    

def transform_likes_city() -> pd.DataFrame:
    """Transform the likes by city data.
    Returns:
        The likes by city DataFrame.
    """
    # initialization
    mongodb_connection = MongoDBConnection()
    
    # get the data from MongoDB
    df_likes_city = pd.DataFrame(mongodb_connection.get_collection("likes_city"))
    # close the MongoDB connection
    mongodb_connection.close()
    
    return df_likes_city

def transform_couverture() -> pd.DataFrame:
    """Transform the couverture of facebook and instagram data.
    Returns:
        The couverture of facebook and instagram DataFrame.
    """
    # initialization
    mongodb_connection = MongoDBConnection()
    
    # get the data from MongoDB
    df_couverture_fb = pd.DataFrame(mongodb_connection.get_collection("couverture_fb"))
    df_couverture_insta = pd.DataFrame(mongodb_connection.get_collection("couverture_insta"))
    # close the MongoDB connection
    mongodb_connection.close()
    
    # merge the data
    df_couverture = pd.merge(
    df_couverture_fb, df_couverture_insta, on="Date", how="inner")
    
    return df_couverture
    
