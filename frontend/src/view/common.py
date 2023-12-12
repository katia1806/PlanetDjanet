# Standard imports
import time

# Intalled imports
import pandas as pd
import streamlit as st
from PIL import Image



@st.cache()
def separate_percentage(df: pd.DataFrame, column: str):
    """Separate and transform a column into percentage in another DataFrame.
    Args:
        df: DataFrame to convert.
        column: Column to convert.
    Returns:
        df_value: DataFrame with the percentage
        df_cp: DataFrame without the percentage column
    """
    # wait for the data to be loaded
    time.sleep(1)
    
    df_cp = df.copy()
    
    # transform the column into a list
    ma_list = list(df_cp[column])
    # remove the percentage sign and replace the comma with a dot
    ma_list = list(map(lambda x: float(x.replace(',', '.').replace('%', '')), ma_list))
    # delete the column
    df_cp.drop([column], axis=1)
    # transform the list of the specific column into a DataFrame with the Valeur as column name
    df_value = pd.DataFrame(ma_list).rename(columns={0: "Valeur"}, index={})
    
    return df_value, df_cp

def get_image(path: str) -> Image:
    """Load an image from the given path.
    Args:
        path: Path of the image file.

    Returns:
        Image: PIL Image object.
    """
    image = Image.open(path)
    return image
