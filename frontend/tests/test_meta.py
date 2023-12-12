# Installed imports
import numpy as np
import pandas as pd
from importlib import reload
from unittest.mock import patch

# Internal imports
from src.controllers.meta_controller import (
    get_couverture_data,
    get_likes_city_data,
    get_likes_gender_age_data,
    get_metrics_data,
    get_pub_data,
    )

@patch('src.controllers.meta_controller.os.getenv', return_value='127.0.0.1')
def test_get_metrics_data(mock_getenv):
    """Test the function get_metrics_data
    """
    from src.controllers import meta_controller
    reload(meta_controller)  # reload the module to mock the os.getenv function
    
    # call the function
    df_insta, df_fb = get_metrics_data()
    
    # check if the data is not empty
    assert not df_insta.empty, "The data of df_insta should not be empty"
    assert not df_fb.empty, "The data of df_fb should not be empty"
    
    # assertions for the type of the returned data
    assert isinstance(df_insta, pd.DataFrame), "The data of df_insta should be a DataFrame"
    assert isinstance(df_fb, pd.DataFrame), "The data of df_fb should be a DataFrame"
    
    # check if each dataframe has the columns of index, Mentions J’aime et réactions, 
    # Commentaires, Partages
    assert ["index", "Mentions J’aime et réactions", "Commentaires", "Partages"] == list(
        df_insta.columns) , "The columns of df_insta should be index, Mentions J’aime et réactions, Commentaires, Partages"
    assert ["index", "Mentions J’aime et réactions", "Commentaires", "Partages"] == list(
        df_fb.columns), "The columns of df_fb should be index, Mentions J’aime et réactions, Commentaires, Partages"
    
    # check the type of the columns
    assert df_insta["index"].dtype == "int64", "The type of the column index of df_insta \
    should be int64"
    assert df_insta["Mentions J’aime et réactions"].dtype == "int64", "The type of the \
    column Mentions J’aime et réactions of df_insta should be int64"
    assert df_insta["Commentaires"].dtype == "int64", "The type of the column Commentaires \
    of df_insta should be int64"
    assert df_insta["Partages"].dtype == "int64", "The type of the column Partages of \
    df_insta should be int64"
    assert df_fb["index"].dtype == "int64", "The type of the column index of df_fb should \
    be int64"
    assert df_fb["Mentions J’aime et réactions"].dtype == "int64", "The type of the column \
    Mentions J’aime et réactions of df_fb should be int64"
    assert df_fb["Commentaires"].dtype == "int64", "The type of the column Commentaires of \
    df_fb should be int64"
    assert df_fb["Partages"].dtype == "int64", "The type of the column Partages of df_fb \
    should be int64"

@patch('src.controllers.meta_controller.os.getenv', return_value='127.0.0.1')
def test_get_pub_data(mock_getenv):
    """Test the function get_pub_data
    """
    from src.controllers import meta_controller
    reload(meta_controller)  # reload the module to mock the os.getenv function
    
    # call the function
    df_pub = get_pub_data()
    
    # check if the data is not empty
    assert not df_pub.empty, "The data of df_pub should not be empty"
    
    # assertions for the type of the returned data
    assert isinstance(df_pub, pd.DataFrame), "The data of df_pub should be a DataFrame"
    
    # check if each dataframe has the columns of _id, "AD_ACCOUNT,IMPRESSION,UNIQUE_USERS" and
    # "AD_ACCOUNT,SPEND,COUNT"
    assert ["_id", "AD_ACCOUNT,IMPRESSION,UNIQUE_USERS", "AD_ACCOUNT,SPEND,COUNT"] == list(
        df_pub.columns), "The columns of df_pub should be _id, \
            AD_ACCOUNT,IMPRESSION,UNIQUE_USERS and AD_ACCOUNT,SPEND,COUNT"
            
    # check the type of the columns
    assert df_pub["_id"].dtype == "object", f"The type of the column _id of df_pub should \
        be object"
    assert df_pub["AD_ACCOUNT,IMPRESSION,UNIQUE_USERS"].dtype == "int64", "The type of the \
        column AD_ACCOUNT,IMPRESSION,UNIQUE_USERS of df_pub should be int64"
    assert df_pub["AD_ACCOUNT,SPEND,COUNT"].dtype == "float", "The type of the column \
        AD_ACCOUNT,SPEND,COUNT of df_pub should be float"
        
@patch('src.controllers.meta_controller.os.getenv', return_value='127.0.0.1')
def test_get_likes_gender_age_data(mock_getenv):
    """Test the function get_likes_gender_age_data
    """
    from src.controllers import meta_controller
    reload(meta_controller)  # reload the module to mock the os.getenv function
    # call the function
    df_likes_gender_age = get_likes_gender_age_data()
    
    # check if the data is not empty
    assert not df_likes_gender_age.empty, "The data of df_likes_gender_age should not be\
        empty"
        
    # assertions for the type of the returned data
    assert isinstance(df_likes_gender_age, pd.DataFrame), "The data of df_likes_gender_age\
        should be a DataFrame"
        
    # check if each dataframe has the columns of _id, Ãge, Femmes, Hommes
    assert ["_id", "Ãge", "Femmes", "Hommes"] == list(
        df_likes_gender_age.columns), "The columns of df_likes_gender_age should be _id, \
            Ãge, Femmes, Hommes"
    
    # check the type of the columns
    assert df_likes_gender_age["_id"].dtype == "object", "The type of the column _id of, \
        df_likes_gender_age should be object"
    assert df_likes_gender_age["Ãge"].dtype == "object", "The type of the column Ãge of  \
        df_likes_gender_age should be object"
    assert df_likes_gender_age["Femmes"].dtype == "object", "The type of the column Femmes of  \
        df_likes_gender_age should be object"
    assert df_likes_gender_age["Hommes"].dtype == "object", "The type of the column Hommes of  \
        df_likes_gender_age should be object"

@patch('src.controllers.meta_controller.os.getenv', return_value='127.0.0.1')
def test_get_likes_city_data(mock_getenv):
    """Test the function get_likes_city_data
    """
    from src.controllers import meta_controller
    reload(meta_controller)  # reload the module to mock the os.getenv function
    # call the function
    df_likes_city = get_likes_city_data()
    
    # check if the data is not empty
    assert not df_likes_city.empty, "The data of df_likes_city should not be empty"
    
    # assertions for the type of the returned data
    assert isinstance(df_likes_city, pd.DataFrame), "The data of df_likes_city should be \
        a DataFrame"
        
    # check if each dataframe has the columns of _id, Ville, Valeur
    assert ["_id", "Principales villes", "Valeur"] == list(
        df_likes_city.columns), "The columns of df_likes_city should be _id, \
            Principales villes, Valeur"
    
    # check the type of the columns
    assert df_likes_city["_id"].dtype == "object", "The type of the column _id of df_likes_city\
        should be object"
    assert df_likes_city["Principales villes"].dtype == "object", "The type of the column \
        Principales villes of df_likes_city should be object"
    assert df_likes_city["Valeur"].dtype == "object", "The type of the column Valeur of \
        df_likes_city should be object"
        
@patch('src.controllers.meta_controller.os.getenv', return_value='127.0.0.1')
def test_get_couverture_data(mock_getenv):
    """Test the function get_couverture_data
    """
    from src.controllers import meta_controller
    reload(meta_controller)  # reload the module to mock the os.getenv function
    # call the function
    df_couverture = get_couverture_data()
    
    # check if the data is not empty
    assert not df_couverture.empty, "The data of df_couverture should not be empty"
    
    # assertions for the type of the returned data
    assert isinstance(df_couverture, pd.DataFrame), "The data of df_couverture should be \
        a DataFrame"
        
    # check if each dataframe has the columns of _id_x, Couverture
    assert ["_id_x", "Date", "Couverture de la Page Facebook", "_id_y", "Couverture Instagram"] == list(
        df_couverture.columns), "The columns of df_couverture should be _id_x, Date, \
            Couverture de la Page Facebook, _id_y, Couverture Instagram"
    
    # check the type of the columns
    assert df_couverture["_id_x"].dtype == "object", "The type of the column _id_x of \
        df_couverture should be object"
    assert df_couverture["Date"].dtype == np.dtype('datetime64[ns]'), "The type of the \
        values in the column Date of df_couverture should be datetime64[ns]"
    assert df_couverture["Couverture de la Page Facebook"].dtype == "int64", "The type of \
        the column Couverture de la Page Facebook of df_couverture should be int64"
    assert df_couverture["_id_y"].dtype == "object", "The type of the column _id_y of \
        df_couverture should be object"
    assert df_couverture["Couverture Instagram"].dtype == "int64", "The type of the column \
        Couverture Instagram of df_couverture should be int64"