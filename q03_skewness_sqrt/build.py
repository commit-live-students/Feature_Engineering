# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    df = data.copy()
    df['GrLivArea'] = np.sqrt(df['GrLivArea'])
    df['SalePrice'] = np.sqrt(df['SalePrice'])
    skw_sale = skew(df['SalePrice'])
    skw_grlv = skew(df['GrLivArea'])
    return skw_grlv,skw_sale


