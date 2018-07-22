# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    housing_data['LotShape'] = LabelEncoder().fit_transform(housing_data['LotShape'])
    dummies = pd.get_dummies(housing_data['GarageType'], prefix='Gar_Type')
    housing_data = pd.concat([housing_data, dummies], axis=1)
    return housing_data

