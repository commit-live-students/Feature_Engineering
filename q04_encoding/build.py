# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder
ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
# Write your code here:
def encoding(df):
    labelencoder = LabelEncoder()
    df['LotShape'] = labelencoder.fit_transform(df['LotShape']) #     encode with label encoder

    # encode with one_hot_encoding
    new_df = pd.get_dummies(df['GarageType'], drop_first=False)
    df = pd.concat([df, new_df], axis=1)

    return df
