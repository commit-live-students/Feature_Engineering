# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(housing_data):
    housing_data=ny_housing[['MasVnrArea','GrLivArea','LotShape','GarageType','SalePrice']]
    mean=housing_data['MasVnrArea'].loc[housing_data['MasVnrArea'].notnull()].mean()
    housing_data['MasVnrArea']=housing_data['MasVnrArea'].fillna(mean)
    highly_occured=housing_data['GarageType'].loc[housing_data['GarageType'].notnull()].value_counts().index[0]
    housing_data['GarageType']=housing_data['GarageType'].fillna(highly_occured)


    housing_data[(housing_data['MasVnrArea']<=housing_data['MasVnrArea'].quantile(0.95)) & (housing_data['GrLivArea']<=housing_data['GrLivArea'].quantile(0.95)) & (housing_data['SalePrice']<=housing_data['SalePrice'].quantile(0.95)) ]



    housing_data['LotShape']=pd.DataFrame(housing_data['LotShape'].reshape(-1,1)).apply(LabelEncoder().fit_transform)
    c=pd.get_dummies(housing_data['GarageType'])
    return pd.concat([housing_data,c],axis=1)
c=encoding(housing_data)
c


