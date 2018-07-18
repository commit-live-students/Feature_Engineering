# %load q04_encoding/build.py
# Default imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def encoding(dataset):
    df = housing_data.copy()
    Lable_encoder = LabelEncoder()
    #df['LotShape'] = pd.get_dummies(df['LotShape'],drop_first=True)
    #df['LotShape'] = Lable_encoder.fit_transform(df['LotShape'])
    #df['GarageType'] = pd.get_dummies(df['GarageType'])
    df= pd.get_dummies(df,drop_first=True)
    return df

