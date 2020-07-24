# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')
housing_data=data[['MasVnrArea','GrLivArea','LotShape','GarageType','SalePrice']]
def skewness_log(data):
    housing_data=data[['MasVnrArea','GrLivArea','LotShape','GarageType','SalePrice']]
    mean=housing_data['MasVnrArea'].loc[housing_data['MasVnrArea'].notnull()].mean()
    housing_data['MasVnrArea']=housing_data['MasVnrArea'].fillna(mean)
    highly_occured=housing_data['GarageType'].loc[housing_data['GarageType'].notnull()].value_counts().index[0]
    housing_data['GarageType']=housing_data['GarageType'].fillna(highly_occured)

    
    housing_data[(housing_data['MasVnrArea']<=housing_data['MasVnrArea'].quantile(0.95)) & (housing_data['GrLivArea']<=housing_data['GrLivArea'].quantile(0.95)) & (housing_data['SalePrice']<=housing_data['SalePrice'].quantile(0.95)) ]

    log_1=np.log(housing_data['SalePrice'])
    log_2=np.log(housing_data['GrLivArea'])
    
#     housing_data['SalePrice']=housing_data['SalePrice'].loc[]
    skew_1=log_1.skew()
    skew_2=log_2.skew()
    return skew_2,skew_1

c=skewness_log(data)
c



