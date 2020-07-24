# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['SalePrice_skew'] = np.sqrt(data['SalePrice'])
    data['GrLivArea_skew'] = np.sqrt(data['GrLivArea'])
    skew_salePrice = skew(data['SalePrice_skew'])
    skew_GrLivArea = skew(data['GrLivArea_skew'])
    return (skew_GrLivArea, skew_salePrice)


