# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(housing_data):

    label_encoder = LabelEncoder()
    housing_data['LotShape'] = label_encoder.fit_transform(housing_data.LotShape)
    housing_data["GarageType"] = housing_data["GarageType"].fillna("None")
    a= pd.get_dummies(housing_data , drop_first= False)
    return a
