# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(ny_housing):
    df = ny_housing
    df['SalePrice'] = np.sqrt(df['SalePrice'])
    df['GrLivArea'] = np.sqrt(df['GrLivArea'])
    return skew(df['GrLivArea']),skew(df['SalePrice'])
skewness_sqrt(ny_housing)


