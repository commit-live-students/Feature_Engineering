# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    encoder = LabelEncoder()
    housing_data['LotShape_Label'] = encoder.fit_transform(housing_data['LotShape'])
    df= pd.get_dummies(housing_data['GarageType'])
    df = pd.concat([housing_data, df], axis=1)
    return df.drop(['GarageType'], axis=1)



