# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(df):
    le = LabelEncoder()
    df['LotShape_Label'] = le.fit_transform(df['LotShape'])
    df=df.join(pd.get_dummies(df['GarageType'], drop_first=True))
    return df




