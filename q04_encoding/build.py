# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import OneHotEncoder
ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(dataset):

    Le = LabelEncoder()
    housing_data['LotShape'] = Le.fit_transform(housing_data['LotShape'])
    df =  pd.get_dummies(housing_data[['GarageType']])
    df = housing_data.join(df)
    return df
encoding(ny_housing)

