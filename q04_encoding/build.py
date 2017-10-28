# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(df):
    le = LabelEncoder()
#     le.fit(housing_data['LotShape'])

    df['LotShape'] = le.fit_transform(housing_data['LotShape'])
    dummies = pd.get_dummies(df['GarageType'])
#     df.drop('GarageType',axis=1,inplace=True)
    return pd.concat([df,dummies],axis=1)
encoding(housing_data)

# Write your code here:
