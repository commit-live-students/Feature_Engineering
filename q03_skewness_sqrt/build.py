# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_sqrt(df):
    df['SalePrice_New'] = np.sqrt(df['SalePrice'])
    df['GrLivArea_New'] = np.sqrt(df['GrLivArea'])
    skewed_slPri = skew(df['SalePrice_New'])
    skewness_grLiv = skew(df['GrLivArea_New'])
    return skewness_grLiv,skewed_slPri
