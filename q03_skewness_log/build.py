# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log(data):
    data['SalePrice'] = np.log(data['SalePrice'])
    data['GrLivArea'] = np.log(data['GrLivArea'])
    val1=skew(data['SalePrice'])
    val2=skew(data['GrLivArea'])
    return val2,val1

#skewness_log(data)
# Write code here:
