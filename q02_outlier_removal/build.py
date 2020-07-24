# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(housing_data):
    df= housing_data.quantile(.95)
    housing_data = housing_data.drop(housing_data [housing_data['GrLivArea'] > df['GrLivArea']].index)
    housing_data = housing_data.drop(housing_data [housing_data['MasVnrArea'] > df['MasVnrArea']].index)
    housing_data = housing_data.drop(housing_data [housing_data['SalePrice'] > df['SalePrice']].index)
    return housing_data




