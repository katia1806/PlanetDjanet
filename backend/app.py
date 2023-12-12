# Intalled imports
from fastapi import FastAPI, HTTPException

# Internal imports
from src.func import (
    transform_insta_publis, 
    transform_facebook_publis, 
    transform_pub,
    transform_likes_city,
    transform_likes_gender_age,
    transform_couverture
    )

app = FastAPI()

@app.get("/meta/metrics")
async def get_meta_metrics():
    """Retrieve metrics data for meta page
    Returns:
        The metrics data.
    """
    # initialisation
    data = {} 
    
    try:
        data["df_insta_publis"] = transform_insta_publis().to_json(orient='records')
        data["df_fb_publis"] = transform_facebook_publis().to_json(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return data

@app.get("/meta/pub")
async def get_meta_metrics():
    """Retrieve pub data for meta page
    Returns:
        The pub data.
    """
    # initialisation
    data = {}     
    
    try:
        data = transform_pub().to_json(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return data

@app.get("/meta/likes_gender_age")
async def get_meta_likes_gender_age():
    """Retrieve likes by gender and age data for meta page
    Returns:
        The likes by gender and age data.
    """
    # initialisation
    data = {}    
    
    try:
        data = transform_likes_gender_age().to_json(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return data

@app.get("/meta/likes_city")
async def get_meta_likes_city():
    """Retrieve likes by city data for meta page
    Returns:
        The likes by city data.
    """
    # initialisation
    data = {}    
    
    try:
        data = transform_likes_city().to_json(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return data

@app.get("/meta/couverture")
async def get_meta_couverture():
    """Retrieve couverture data for meta page
    Returns:
        The couverture data.
    """
    # initialisation
    data = {}    
    
    try:
        data = transform_couverture().to_json(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return data