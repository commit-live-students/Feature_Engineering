# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
from sklearn.preprocessing import LabelEncoder

# Write your code here:
def encoding(housing_data):
    lablel_encoder = LabelEncoder()
    housing_data['LotShape_Label'] = lablel_encoder.fit_transform(housing_data['LotShape'])
    return pd.get_dummies(housing_data, columns = ['GarageType'])

encoding(housing_data)


