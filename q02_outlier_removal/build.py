# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import Imputer
import numpy as np

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
housing_data_columns=['MasVnrArea', 'GrLivArea', 'SalePrice']
# Write your code here:
def outlier_removal(housing_data):

    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    housing_data['MasVnrArea'] = imp_mean.fit_transform(housing_data[['MasVnrArea']])
    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])
    IQRU=list()
    for c in housing_data_columns:
        IQRU.append([c,housing_data[c].quantile(0.95)])
    for c in IQRU:
        housing_data=housing_data.drop(housing_data[(housing_data[c[0]]>c[1])].index)
    return housing_data


