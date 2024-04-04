
import pandas as pd

# Function to filer on countries
def filter_europe(df, column_name='', countries=[]):
    return df[df[column_name].isin(countries)]

