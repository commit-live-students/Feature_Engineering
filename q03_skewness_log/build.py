# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['GrLivArea'] = np.log(data['GrLivArea'])
    sv1 = skew(data['GrLivArea'])
    data['SalePrice'] = np.log(data['SalePrice'])
    sv2 = skew(data['SalePrice'])
    return sv1, sv2
data.head()


