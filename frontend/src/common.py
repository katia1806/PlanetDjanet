
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

def by_month(data, year, column):
    """Aggregate data by month for a specific year."""
    agg_by_month = data[data["year"] == year].groupby("month")[column].sum()
    return pd.DataFrame(agg_by_month).reset_index()

def by_week(data, year, column):
    """Aggregate data by week for a specific year."""
    agg_by_week = data[data["year"] == year].groupby("week")[column].sum()
    return pd.DataFrame(agg_by_week).reset_index()