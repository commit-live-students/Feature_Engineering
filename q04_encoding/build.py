# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(df):
    #df = df[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
    le = LabelEncoder()


    #df['GarageType'] = le.fit_transform(df['GarageType'])
    df['LotShape'] = le.fit_transform(df['LotShape'])
    df_garage = pd.get_dummies(df['GarageType'])
    #df.drop(['GarageType'],axis=1,inplace=True)
    df_new = pd.concat([df,df_garage],ignore_index=True,axis=1)
    return df_new
