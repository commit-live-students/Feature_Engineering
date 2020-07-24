# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log(df):
    df_trans = df.copy()
    df_trans['SalePrice'] = np.log(df_trans['SalePrice'])
    df_trans['GrLivArea'] = np.log(df_trans['GrLivArea'])
    return skew(df_trans['GrLivArea']), skew(df_trans['SalePrice'])



