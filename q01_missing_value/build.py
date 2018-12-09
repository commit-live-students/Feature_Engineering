# %load q01_missing_value/build.py
# Default imports
import pandas as pd
import numpy as np
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
def imputation(housing_data):
    missing = housing_data.isnull().sum(axis=0).sort_values(ascending=False)
    housing_data['MasVnrArea'].replace(0, np.nan, inplace= True)
    housing_data['GarageType'] = housing_data['GarageType'].fillna('Attchd')
    housing_data['MasVnrArea'] = housing_data['MasVnrArea'].fillna(housing_data['MasVnrArea'].mean())
    return housing_data[['MasVnrArea']], housing_data[['GarageType']]

imputation(housing_data)


