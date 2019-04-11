# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def encoding(dataset):
    le = LabelEncoder()
    dataset['LotShape'] =  dataset['LotShape'].fillna(dataset['LotShape'].mode()[0])
    dataset['GarageType'] =  dataset['GarageType'].fillna(dataset['GarageType'].mode()[0])
    dataset['LotShape_Label'] = le.fit_transform(dataset['LotShape'])
    df_dummy = pd.get_dummies(dataset['GarageType'])
    dataset = dataset.drop(['GarageType'],1)
    dataset = pd.concat([dataset,df_dummy],1)
    return dataset











