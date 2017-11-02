# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(housing_data):
    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].value_counts().idxmax())
    housing_data['LotShape'] = housing_data['LotShape'].fillna(housing_data['LotShape'].value_counts().idxmax())
    housing_data['MasVnrArea'] = housing_data['MasVnrArea'].fillna(housing_data['MasVnrArea'].mean())
    housing_data['GrLivArea'] = housing_data['GrLivArea'].fillna(housing_data['GrLivArea'].mean())
    df1 = housing_data[['MasVnrArea','GrLivArea']]
    df2 = housing_data[['LotShape', 'GarageType']]
    return df1,df2
