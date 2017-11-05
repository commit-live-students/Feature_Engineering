# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')
def skewness_log(df):
    #return df
    df_trans=df.copy()
    df_trans['GrLivArea'] = np.log(df_trans['GrLivArea'])
    skewness_grLiv = skew(df_trans['GrLivArea'])
    #print(skewness_grLiv)
    df_trans['SalePrice'] = np.log(df_trans['SalePrice'])
    skewness_saleprice = skew(df_trans['SalePrice'])
    return skewness_grLiv, skewness_saleprice
