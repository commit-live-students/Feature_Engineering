# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    columnsToEncode = list(housing_data.select_dtypes(include=['category','object']))
    le=LabelEncoder()
    housing_data['newLotShape']=le.fit_transform(housing_data[columnsToEncode[0]])
    ld=pd.get_dummies(housing_data[columnsToEncode[1]], drop_first=True)
    frames = [housing_data,ld]
    result = pd.concat(frames,axis=1)
    return result    


