# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(df):
    df['GrLivAreaSqr'] = np.sqrt(df['GrLivArea'])
    sv1 = skew(df['GrLivAreaSqr'])
    df['SalePriceSqr'] = np.sqrt(df['SalePrice'])
    sv2 = skew(df['SalePriceSqr'])
    return sv1, sv2



