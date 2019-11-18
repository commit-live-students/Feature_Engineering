# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    le = LabelEncoder()
    dataset['LotShape'] = le.fit_transform(dataset['LotShape'])
    return dataset.add(pd.get_dummies(housing_data['GarageType']))



