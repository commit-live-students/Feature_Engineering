# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    df_trans=data.copy()
    df_trans['newGrLivArea'] = np.log(df_trans['GrLivArea'])
    df_trans['newSalePrice']  =np.log(df_trans['SalePrice']) 
    
    skewed_grLiv = skew(df_trans['newGrLivArea'])
    skewed_salePrice = skew(df_trans['newSalePrice'])
    return skewed_grLiv,skewed_salePrice
    

