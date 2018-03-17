from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['SalePrice'] = np.log(data['SalePrice'])
    data['GrLivArea'] = np.log(data['GrLivArea'])
    return skew(data['GrLivArea']), skew(data['SalePrice'])
