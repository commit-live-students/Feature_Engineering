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
    cat=housing_data[['LotShape','GarageType']]
    num=housing_data[['MasVnrArea','GrLivArea']]
    #x=['Attchd']
    cat[['GarageType']]=cat[['GarageType']].fillna('Attchd')
    #housing_data[['GarageType']].isnull().any()
    num['MasVnrArea'].isnull().any()
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(num[['MasVnrArea']])
    num[['MasVnrArea']] = imp_mean.transform(housing_data[['MasVnrArea']])
    #housing_data[['GarageType']].isnull().any()
    return num,cat
