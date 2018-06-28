# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    
    df_trans=data.copy()
    df_trans['GrLivArea'] = np.log(df_trans['GrLivArea'])
    df_trans['SalePrice'] = np.log(df_trans['SalePrice'])
    
    
    skewness_grLiv = skew(df_trans['GrLivArea'])
    skewness_saleprice= skew(df_trans['SalePrice'])
    return skewness_grLiv,skewness_saleprice
    
    
skewness_log(data)


