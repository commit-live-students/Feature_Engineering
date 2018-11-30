# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    
    label = LabelEncoder()
    dataset['LotShape_Label'] = label.fit_transform(dataset.LotShape)
    dataset.drop('LotShape',axis=1,inplace = True)
    df = pd.get_dummies(housing_data.GarageType)
    dataset = pd.concat([housing_data,df],axis=1)
    
    return dataset

encoding(housing_data)



