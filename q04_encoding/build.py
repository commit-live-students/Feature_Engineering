import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import OneHotEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df):
    le=LabelEncoder()

    #df['LotShape']=le.fit_transform(df['LotShape'])
    #print(df)
    #lb=LabelBinarizer()
    df.loc[:,'LotShape']=le.fit_transform(df.loc[:,'LotShape'])
    #print(df['LotShape'])
    df.GarageType=le.fit_transform(df.GarageType)

    df1=pd.get_dummies(df['GarageType'], drop_first=True)
    #print(df1)
    d2=pd.concat([df1,df],join='outer',axis=1)
    #print(type(d2))
    return d2
