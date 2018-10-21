# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')
def skewness_log(data):

    data['GrLivArea'] = np.log(data['GrLivArea'])
    data['SalePrice'] = np.log(data['SalePrice'])

    return skew(data['GrLivArea']),skew(data['SalePrice'])
skewness_log(data)


