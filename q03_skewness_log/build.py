from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['GrLivAr'] = np.log(data['GrLivArea'])
    data['SalePric'] = np.log(data['SalePrice'])
    skewed_GrLivAr = skew(data['GrLivAr'])
    skewed_SalePric = skew(data['SalePric'])
    return skewed_GrLivAr, skewed_SalePric
