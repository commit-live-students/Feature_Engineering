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
    df = housing_data
    imp = Imputer(missing_values=float('NaN'),strategy='mean', axis=0)
    df['MasVnrArea'] = imp.fit_transform(df[['MasVnrArea']])
    df['GrLivArea'] = imp.fit_transform(df[['GrLivArea']])
    df['SalePrice'] = imp.fit_transform(df[['SalePrice']])
    df['LotShape'] = df['LotShape'].fillna(df['LotShape'].mode()[0])
    df['GarageType'] = df['GarageType'].fillna(df['GarageType'].mode()[0])
    return df[['MasVnrArea', 'GrLivArea', 'SalePrice']],df[['LotShape', 'GarageType']]
#imputation(housing_data)


