# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(ds):
    cat_cols = list(ds.select_dtypes(include=['category','object']))
    #print cat_cols
    le = LabelEncoder()
    ds["LotShape"]=le.fit_transform(ds["LotShape"])
    #print ds.shape
    #print le.classes_
    #ohe = OneHotEncoder()
    ds_garage=pd.get_dummies(ds["GarageType"], drop_first=False)
    #ohe.fit_transform(ds["GarageType"])
    #print ohe.classes_
    final = pd.concat([ds, ds_garage], axis=1)
    return final
