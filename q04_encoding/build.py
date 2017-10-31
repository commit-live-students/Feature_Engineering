# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(housing_data):
    #df = housing_data
    #columnsToEncode = list(df.select_dtypes(include=['category','object']))
    #le = LabelEncoder()
    df = pd.get_dummies( housing_data, drop_first = True )
  #  for feature in columnsToEncode:

    #    try:
        #    df[feature] = le.fit_transform(df[feature])
   #     except:
        #     print('Error encoding '+feature)
    return df
# Write your code here:
