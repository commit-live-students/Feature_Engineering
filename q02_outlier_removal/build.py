# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(df):

    num_columns =df.select_dtypes(include=['float64','int64'])
    quantile_95= num_columns.quantile(0.95)
    for colname in num_columns:
        quantile = quantile_95[colname]
        df=df.drop(df[df[colname]>quantile].index)
    return df


