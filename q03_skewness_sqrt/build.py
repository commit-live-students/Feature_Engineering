# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_sqrt(data):
    data['SalePrice'] = np.sqrt(data['SalePrice'])
    data['GrLivArea'] = np.sqrt(data['GrLivArea'])
    val1=skew(data['SalePrice'])
    val2=skew(data['GrLivArea'])
    return val2,val1


# Write code here:
