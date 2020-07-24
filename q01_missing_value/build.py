# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')

housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


def imputation(data):
    model_mean = Imputer(missing_values = 'NaN', strategy='most_frequent')
    model_mean.fit(data[['MasVnrArea']])
    data['MasVnrArea']=model_mean.transform(data[['MasVnrArea']])
    data['GarageType'].fillna(data['GarageType'].mode()[0],inplace=True)
    return data[['MasVnrArea','GrLivArea']],data[['LotShape','GarageType']]


