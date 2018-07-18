# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    df = data.copy()
    
    df['GrLivArea'] = np.log(df['GrLivArea'])
    df['SalePrice'] = np.log(df['SalePrice'])
    skw_sale = skew(df['SalePrice'])
    skw_grlv = skew(df['GrLivArea'])
    return skw_grlv,skw_sale

