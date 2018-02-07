# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    housing_data["LotShape"] = housing_data["LotShape"].astype('category')
    label_encoder = LabelEncoder()
    housing_data["LotShape_label"] = label_encoder.fit_transform(housing_data["LotShape"])
    housing_data = pd.get_dummies(housing_data, columns=['GarageType'])
    return housing_data
