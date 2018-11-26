# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['GrLivArea'] = np.sqrt(data['GrLivArea'])
    data['SalePrice'] = np.sqrt(data['SalePrice'])
    sk_val1 = skew(data['GrLivArea'])
    sk_val2 = skew(data['SalePrice'])
    return sk_val1, sk_val2 







