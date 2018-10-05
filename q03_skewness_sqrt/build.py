# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')
housing_data=ny_housing[['MasVnrArea','GrLivArea','LotShape','GarageType','SalePrice']]
def skewness_sqrt(ny_housing):
    housing_data=ny_housing[['MasVnrArea','GrLivArea','LotShape','GarageType','SalePrice']]
    mean=housing_data['MasVnrArea'].loc[housing_data['MasVnrArea'].notnull()].mean()
    housing_data['MasVnrArea']=housing_data['MasVnrArea'].fillna(mean)
    highly_occured=housing_data['GarageType'].loc[housing_data['GarageType'].notnull()].value_counts().index[0]
    housing_data['GarageType']=housing_data['GarageType'].fillna(highly_occured)

    
    housing_data[(housing_data['MasVnrArea']<=housing_data['MasVnrArea'].quantile(0.95)) & (housing_data['GrLivArea']<=housing_data['GrLivArea'].quantile(0.95)) & (housing_data['SalePrice']<=housing_data['SalePrice'].quantile(0.95)) ]
    
    s1=np.sqrt(housing_data['SalePrice'])
    s2=np.sqrt(housing_data['GrLivArea'])
    
    skew1=s1.skew()
    skew2=s2.skew()
    
    return skew2,skew1

c= skewness_sqrt(ny_housing)
c



