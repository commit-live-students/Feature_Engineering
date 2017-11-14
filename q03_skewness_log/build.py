# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')
data=ny_housing


def skewness_log(data):
    data['SalePrice'] = np.log(data['SalePrice'])
    data['GrLivArea'] = np.log(data['GrLivArea'])

    skew_1 = skew(data['GrLivArea'])
    skew_2 = skew(data['SalePrice'])

    return skew_1, skew_2

# Write code here:
#skewness_log(data)
