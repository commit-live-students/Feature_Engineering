# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(data):
    le = LabelEncoder()
    data['LotShape'] = le.fit_transform(data['LotShape'])
    data = pd.get_dummies(data,dummy_na=True)
    return data
#encoding(housing_data)


