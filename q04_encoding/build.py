# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    lablel_encoder = LabelEncoder()
# housing_data['LotShape'] = lablel_encoder.fit_transform(housing_data['LotShape'])

# housing_data['GarageType'] = lablel_encoder.fit_transform(housing_data['GarageType'])
    df = pd.get_dummies(housing_data , drop_first= True)
    return df
encoding(housing_data)


