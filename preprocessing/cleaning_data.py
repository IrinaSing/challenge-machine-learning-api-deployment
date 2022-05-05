# Code for data cleaning

import pandas as pd

# func that puts outliers into list
def outliers(df, ft):
    Q1 = df[ft].quantile(0.25)
    Q3 = df[ft].quantile(0.60)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # list to store indexes of outliers
    ls = df.index[(df[ft] < lower_bound) | (df[ft] > upper_bound)]
    return ls



# function that removes outliers
def remove_outliers(df, ls):
    ls = sorted(set(ls))
    df = df.drop(ls)
    return df


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
    df = df.dropna()

    # sq meter price
    df1 = df.copy()
    df1['Price_per_sq'] = df1['Price'] / df1['Living_area']
    
    # create an empty list to store the output indices from multiple columns
    index_list = []
    for feature in ['Living_area', 'Surface_area_land', 'Price_per_sq', 'Number_of_bedrooms', 'Price']:
        index_list.extend(outliers(df1, feature))

    df_clean = remove_outliers(df1, index_list)
    
    # reduce amount of unpopular locations
    location_stat = df_clean.groupby('Location')['Location'].agg('count').sort_values(ascending=False)
    loc_less_10 = location_stat[location_stat<=10]
    df_clean.Location = df_clean.Location.apply(lambda x: 'Other' if x in loc_less_10 else x)
    df_clean1 = df_clean.drop(['Price_per_sq'], axis='columns')

    df_clean1.to_csv('clean_df.csv')
    # return df_clean1
    # print(df_clean1.shape)

preprocess()