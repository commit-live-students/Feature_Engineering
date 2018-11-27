# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')
def skewness_log(data): 
    data_trans=data.copy()
    data_trans['GrLivArea']=np.log(data_trans['GrLivArea'])
    data_trans['SalePrice']=np.log(data_trans['SalePrice'])
    return(skew(data_trans['GrLivArea']),skew(data_trans['SalePrice']))
skewness_log(data)

