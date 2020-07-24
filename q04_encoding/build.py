# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df):
    df_trans = df.copy()
    #print(df_trans.info())
    #Encode LotShape using LabelEncoder and assign to LotShape_Label
    columnsToEncode = ['LotShape']#list(df_trans.select_dtypes(include=['category','object']))
    #print(columnsToEncode)
    le = LabelEncoder()
    for feature in columnsToEncode:
     #   print(feature)
        try:
            df_trans[feature+'_Label'] = le.fit_transform(df_trans[feature])
        except:
            print('Error encoding '+feature)
    #Create dummies for GarageType
    newCols = pd.get_dummies(df_trans['GarageType'], drop_first=True)
    df_trans = pd.concat([df_trans,newCols], axis=1)
    return df_trans

