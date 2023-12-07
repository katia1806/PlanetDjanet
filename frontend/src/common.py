# Related third party imports
import pandas as pd

def by_month(data, year, column):
    """Aggregate data by month for a specific year."""
    agg_by_month = data[data["year"] == year].groupby("month")[column].sum()
    return pd.DataFrame(agg_by_month).reset_index()

def by_week(data, year, column):
    """Aggregate data by week for a specific year."""
    agg_by_week = data[data["year"] == year].groupby("week")[column].sum()
    return pd.DataFrame(agg_by_week).reset_index()