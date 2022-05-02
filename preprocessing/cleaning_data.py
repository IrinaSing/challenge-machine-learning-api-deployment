# Code for data cleaning

# Code for data cleaning

import pandas as pd

def preprocess():
    url = 'https://raw.githubusercontent.com/IrinaSing/challenge-collecting-data-immo/main/data/houses.csv'
    df = pd.read_csv(url, index_col=0)

    df.columns = [c.replace(' ', '_') for c in df.columns]
    
    # exclude columns which are insignificant
    df = df.drop(['Terrace_orientation','Garden_orientation', 'Property_type', 'Property_subtype', 'Type_of_sale', 'Number_of_facades', 'Kitchen'], axis=1) 
    
    # include only rows where price is not 0
    df = df[df['Price'].notna()]
    df['Pool'] = df['Pool'].fillna(False)
    df["Terrace"].replace({"Unknown": False}, inplace=True)
    df["Garden"].replace({"Unknown": False}, inplace=True)
    df['Furnished'] = df['Furnished'].fillna(False)

    # sq meter price
    df1 = df.copy()
    df1['Price_per_sq'] = df1['Price'] / df1['Living_area']
    location_stat = df.groupby('Location')['Location'].agg('count').sort_values(ascending=False)

    # reduce amount of unpopular locations
    loc_less_10 = location_stat[location_stat<=10]
    df1.Location = df1.Location.apply(lambda x: 'Other' if x in loc_less_10 else x)

    return df1
