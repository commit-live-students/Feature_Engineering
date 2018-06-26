# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['SalePrice_logTrans'] = np.log(data['SalePrice'])
    data['GrLivArea_logTrans'] = np.log(data['GrLivArea'])
    skew_SalePrice = skew(data['SalePrice_logTrans'])
    skew_GrLivArea = skew(data['GrLivArea_logTrans'])
    return skew_GrLivArea, skew_SalePrice

#skewness_log(data)

