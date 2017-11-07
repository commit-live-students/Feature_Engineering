# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    le = LabelEncoder()
    housing_data['LotShape'] = le.fit_transform(housing_data['LotShape'])
    housing_data['GarageType'] = le.fit_transform(housing_data['GarageType'])
    enc = OneHotEncoder()
    enc.fit(housing_data['GarageType'].reshape(-1,1))
    onehotlabels = enc.transform(housing_data['GarageType'].reshape(-1,1)).toarray()
    c = pd.DataFrame(onehotlabels)
    housing_data = housing_data.join(c)
    del housing_data['GarageType']

    return housing_data
