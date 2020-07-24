# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    df = data
    df['SalePrice'] = np.log(df['SalePrice'])
    df['GrLivArea'] = np.log(df['GrLivArea'])
    return skew(df['GrLivArea']),skew(df['SalePrice'])
skewness_log(data)


