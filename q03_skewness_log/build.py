# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    df= data.copy()
    df['GrLivArea_t']= np.log(df['GrLivArea'])
    df['SalePrice_t']= np.log(df['SalePrice'])
    skewness_grLiv = skew(df['GrLivArea_t'])
    skewness_slpr = skew(df['SalePrice_t'])
    return skewness_grLiv,skewness_slpr


