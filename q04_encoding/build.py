# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]



#Write your solution here :
def encoding(df):
    le = LabelEncoder()
    df['Count'] = 1
    df['LotShape'] = le.fit_transform(df['LotShape'])
    df = pd.get_dummies(df, columns=['GarageType'])
    
    return df

#encoding(housing_data)


