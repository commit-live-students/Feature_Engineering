# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(housing_data):
    total12=housing_data[housing_data.notnull()]
    le = LabelEncoder()
    #total12['GarageType_label']=total12['GarageType'].fillna('null')
    total12=pd.concat([total12,pd.get_dummies(total12['GarageType'],prefix=['GarageType_Label'],dummy_na=False,drop_first=False)],axis=1).drop('GarageType',1)
    total12['LotShape_label']=le.fit_transform(total12['LotShape'])
    return(total12)
encoding(housing_data)

