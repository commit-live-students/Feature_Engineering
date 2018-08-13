# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    skewness_SpLiv1 = skew(data['SalePrice'])
    skewness_grLiv1 = skew(data['GrLivArea'])
    data['SalePrice'] = np.log(data['SalePrice'])
    data['GrLivArea'] = np.log(data['GrLivArea'])
    skewness_SpLiv2 = skew(data['SalePrice'])
    skewness_grLiv2 = skew(data['GrLivArea'])
    return skewness_grLiv2,skewness_SpLiv2

skewness_log(data)

