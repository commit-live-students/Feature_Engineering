# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    le =LabelEncoder()
    housing_data['LotShape'] = le.fit_transform(housing_data['LotShape'])
    housing_data= pd.get_dummies(housing_data, columns=['GarageType'])
    housing_data['count'] = 1
    return housing_data
encoding(housing_data)




