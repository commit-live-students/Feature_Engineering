# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(df):
    df_trans = df.copy()
    df_trans['SalePrice'] = np.sqrt(df_trans['SalePrice'])
    df_trans['GrLivArea'] = np.sqrt(df_trans['GrLivArea'])
    return skew(df_trans['GrLivArea']), skew(df_trans['SalePrice'])



