# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['GrLivArea'] = np.log(data['GrLivArea'])
    data['SalePrice'] = np.log(data['SalePrice'])
    sk_val1 = skew(data['GrLivArea'])
    sk_val2 = skew(data['SalePrice'])
    return sk_val1, sk_val2 




