# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    lablel_encoder = LabelEncoder()
    housing_data['LotShape_Label'] = lablel_encoder.fit_transform(housing_data['LotShape'])
    
    dummies=pd.get_dummies(housing_data['GarageType'])
    new_data=pd.concat([housing_data, dummies], axis = 1)
    new_data=new_data.drop('GarageType',axis=1)
    return new_data
    
    


