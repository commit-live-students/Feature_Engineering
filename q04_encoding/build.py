# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def encoding(dataset):
    df=housing_data.loc[:,['LotShape','GarageType']]
    #df['LotShape'] = LabelEncoder().fit_transform(df['LotShape'])
    df2=housing_data.loc[:,['MasVnrArea', 'GrLivArea', 'SalePrice']]
    df1=pd.get_dummies(df, drop_first=True)
    #df_final=pd.concat([df['LotShape'],])
    #df['GarageType'] = LabelEncoder().fit_transform(df['GarageType'])
    return pd.concat([df1,df2],axis=1)
