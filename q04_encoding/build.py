# Default imports
import pandas as pd
from sklearn import preprocessing

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def encoding(data):
    le = preprocessing.LabelEncoder()
    housing_data['Lotshape'] = le.fit_transform(housing_data['LotShape'])#housing_data.LotShape
    housing = pd.get_dummies(housing_data['GarageType'])
    result = pd.concat([housing_data, housing], axis=1)
    del result['LotShape']
    return result
