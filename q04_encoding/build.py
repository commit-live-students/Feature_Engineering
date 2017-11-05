# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(df):
    #return df
    lablel_encoder = LabelEncoder()
    df['GarageType'] = lablel_encoder.fit_transform(df['GarageType'])
    #return df['LotShape']
#     df['GarageType'] = lablel_encoder.fit_transform(df['GarageType'])
#     return df
    #df1 = df.loc[:, df.columns != 'LotShape']
    x = pd.get_dummies(df['LotShape'])
    y = pd.get_dummies(df['GarageType'])
    df2 = pd.concat([x, y], axis = 1)

    return df2
