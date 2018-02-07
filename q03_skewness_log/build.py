from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['GrLivArea1'] = np.log(data['GrLivArea'])
    data['SalePrice1'] = np.log(data['SalePrice'])
    skewed_GrLivArea1 = skew(data['GrLivArea1'])
    skewed_SalePrice1 = skew(data['SalePrice1'])
    return skewed_GrLivArea1, skewed_SalePrice1
