# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(df):
    quantiles = df.quantile(q=0.95,axis=0)
    for col in quantiles.index:
        df[col] = df.drop(df[(df[col]>quantiles[col])].index, inplace=True)
    return df


