import pandas as pd
from sklearn.preprocessing import Imputer
import warnings

ny_housing = pd.read_csv('./data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(housing_data):
    
    housing_data['MasVnrArea'] = housing_data['MasVnrArea'].fillna(housing_data['MasVnrArea'].mean())
    housing_data['GrLivArea'] = housing_data['GrLivArea'].fillna(housing_data['GrLivArea'].mean())
    housing_data['SalePrice'] = housing_data['SalePrice'].fillna(housing_data['SalePrice'].mean())
    
    housing_data['LotShape'] = housing_data['LotShape'].fillna(housing_data['LotShape'].mode()[0])
    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])
    
    return housing_data[['MasVnrArea', 'GrLivArea', 'SalePrice']], housing_data[['LotShape', 'GarageType']]

imputation(housing_data)





