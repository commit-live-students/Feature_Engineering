# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


def skewness_sqrt(data):
    data['SalePrice'] = np.sqrt(data['SalePrice'])
    data['GrLivArea'] = np.sqrt(data['GrLivArea'])
    skew_sp = skew(data['SalePrice'])
    skew_gra = skew(data['GrLivArea'])
    return skew_gra, skew_sp


