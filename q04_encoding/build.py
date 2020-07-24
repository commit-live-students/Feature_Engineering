# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df1):
    df=df1.copy()
    le = LabelEncoder()
    df['LotShape'] = le.fit_transform(df['LotShape'])
    res=pd.get_dummies(df, drop_first=False)
    res['GarageType']=df['GarageType']
    return res


