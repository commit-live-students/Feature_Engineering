# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    
    data['log_SalePrice']=np.log(data['SalePrice'])
    data['log_GrLivArea']=np.log(data['GrLivArea'])
        
    return skew(data['log_GrLivArea']),skew(data['log_SalePrice'])
skewness_log(data)



