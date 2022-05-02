# Code for data cleaning

# Code for data cleaning

import pandas as pd

def preprocess():
    url = 'https://raw.githubusercontent.com/IrinaSing/challenge-collecting-data-immo/main/data/houses.csv'
    df = pd.read_csv(url, index_col=0)

    # include only rows where price is not 0
    df = df[df['Price'].notna()]
    df.columns = [c.replace(' ', '_') for c in df.columns]
    # exclude columns which are insignificant
    df = df.drop(['Terrace_orientation','Garden_orientation', 'Property_type', 'Property_subtype', 'Type_of_sale', 'Number_of_facades', 'Kitchen'], axis=1) 
    df['Pool'] = df['Pool'].fillna(False)
    df["Terrace"].replace({"Unknown": False}, inplace=True)
    df["Garden"].replace({"Unknown": False}, inplace=True)
    df['Furnished'] = df['Furnished'].fillna(False)

    return df
