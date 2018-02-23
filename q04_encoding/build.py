# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def encoding(dataset):
    le = LabelEncoder()
    dataset['LotShape'] = le.fit_transform(dataset['LotShape'])
    df=dataset.copy()
    GT=pd.get_dummies(dataset['GarageType'])
    return pd.concat([df,GT],axis=1)
