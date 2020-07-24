# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

data = pd.read_csv('data/train.csv')
def skewness_sqrt(data): 
    data_trans=data.copy()
    data_trans['GrLivArea']=np.sqrt(data_trans['GrLivArea'])
    data_trans['SalePrice']=np.sqrt(data_trans['SalePrice'])
    return(skew(data_trans['GrLivArea']),skew(data_trans['SalePrice']))
skewness_sqrt(data)


