# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:

def skewness_sqrt(df):
    df_trans = df.copy()
    df_trans['GrLivArea'] = np.sqrt(df_trans['GrLivArea'])
    df_trans['SalePrice'] = np.sqrt(df_trans['SalePrice'])
    skewness_grLiv = skew(df_trans['GrLivArea'])
    skewness_slpr = skew(df_trans['SalePrice'])
    return skewness_grLiv,skewness_slpr


