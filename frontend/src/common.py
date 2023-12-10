# Standard imports
import time

# Intalled imports
import pandas as pd
import streamlit as st

def display_social_media_links():
    """Display social media links in the sidebar."""
    # display the title
    st.sidebar.markdown("Social Media Links")
    
    # display the social media links
    col1, col2, col3 = st.sidebar.columns(3)
    # Instagram Link
    col1.markdown('''
        <a href="https://www.instagram.com/planet___djanet/?hl=fr">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/240px-Instagram_icon.png" width="50" height="50" />
        </a>''',
                unsafe_allow_html=True
                )
    # Facebook Link
    col2.markdown('''
        <a href="https://www.facebook.com/PlanetDjanet/">
            <img src="https://cdn-icons-png.flaticon.com/512/124/124010.png" width="50" height="50" />
        </a>''',
                unsafe_allow_html=True
                )
    # Twitter Link
    col3.markdown('''
        <a href="https://planetdjanet.com/fr/">
            <img src="http://planetdjanet.com/wp-content/uploads/2020/06/logo2.0._blanc_noback.png" width="80" height="50" />
        </a>''',
                unsafe_allow_html=True
                )

def by_month(df, year:int, column:str) -> pd.DataFrame:
    """Aggregate data by month for a specific year.
    Args:
        df: DataFrame to aggregate.
        year: Year to aggregate.
        column: Column to aggregate.
    Returns:
        DataFrame with the data aggregated by month.
    """
    agg_by_month = df[df["year"] == year].groupby("month")[column].sum()
    
    return pd.DataFrame(agg_by_month).reset_index()

def by_week(df:pd.DataFrame, year:int, column:str) -> pd.DataFrames:
    """Aggregate data by week for a specific year.
    Args:
        df: DataFrame to aggregate.
        year: Year to aggregate.
        column: Column to aggregate.
    Returns:
        DataFrame with the data aggregated by week.
    """
    agg_by_week = df[df["year"] == year].groupby("week")[column].sum()
    
    return pd.DataFrame(agg_by_week).reset_index()

def to_date(df: pd.DataFrame) -> pd.DataFrame:
    """Convert the 'Date' column of a DataFrame to datetime format.
    Args:
        df: DataFrame to convert.
    Returns:
        df: DataFrame with the 'Date' column converted to datetime format.
    """
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
    
    return df

@st.cache()
def separate_percentage(df: pd.DataFrame, column: str) -> tuple(pd.DataFrame, pd.DataFrame):
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