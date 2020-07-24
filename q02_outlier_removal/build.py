# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
# def outlier_removal(df):
#     numeric_features = df.select_dtypes(include = ['float64', 'int64'])
#     quantile_values = numeric_features.quantile(0.95)
#     for feature in list(numeric_features):
#         df = df.drop(df[df[feature] > quantile_values[feature]].index)
#     return df

def outlier_removal(df):
    numeric_features = df.select_dtypes(include = ['float64', 'int64'])
    quantile_values = numeric_features.quantile(0.95)
    for feature in list(numeric_features):
        df = df[df[feature]<=quantile_values[feature]]
    return df

len(outlier_removal(housing_data))








