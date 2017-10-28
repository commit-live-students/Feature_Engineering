# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding (dataset):
    label_enc= LabelEncoder()
    a = pd.get_dummies(housing_data['GarageType'], drop_first=True)
    housing_data['LotShape'] = label_enc.fit_transform(housing_data['LotShape'])
    b = housing_data['LotShape']
    df_new = pd.concat([housing_data,a,b], axis = 1)
    return df_new
