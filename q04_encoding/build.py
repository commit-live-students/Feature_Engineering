# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(housing_data):
    lablel_encoder = LabelEncoder()
    housing_data['LotShape_Label'] = lablel_encoder.fit_transform(housing_data['LotShape'])
    df = pd.get_dummies(housing_data['GarageType'])
    housing_data = pd.concat([housing_data,df] , axis=1)
    housing_data= housing_data.drop('GarageType', axis=1)
    return housing_data


