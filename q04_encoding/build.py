# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df):
    columnsToEncode = list(df.select_dtypes(include=['category','object']))
    le = LabelEncoder()
    df['LotShape_Label'] = le.fit_transform(df['LotShape'])
    df=pd.concat([df, pd.get_dummies(df['GarageType'])], axis=1);
    df.drop('GarageType', axis=1, inplace = True)
    return df

housing_data

