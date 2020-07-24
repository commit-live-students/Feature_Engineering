# %load q01_missing_value/build.py
# Default imports
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(ny_housing):
#     mean=housing_data['MasVnrArea'].loc[housing_data['MasVnrArea'].notnull()].mean()
#     housing_data['MasVnrArea']=housing_data['MasVnrArea'].fillna(mean)
#     highly_occured=housing_data['GarageType'].loc[housing_data['GarageType'].notnull()].value_counts().index[0]
#     housing_data['GarageType']=housing_data['GarageType'].fillna(highly_occured)
#     return housing_data[['MasVnrArea','GarageType']]

    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(housing_data[['MasVnrArea']])
    housing_data[['MasVnrArea']] = imp_mean.transform(housing_data[['MasVnrArea']])
    housing_data['GarageType'] =  housing_data['GarageType'] .fillna( housing_data['GarageType'].mode()[0])
    return pd.DataFrame(housing_data['MasVnrArea']),pd.DataFrame(housing_data['GarageType'])
c=imputation(ny_housing)
c







