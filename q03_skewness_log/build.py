from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['SalePrice1'] = np.log(data['SalePrice'])
    data['GrLivArea1'] = np.log(data['GrLivArea'])
    skew_SalePrice = skew(data['SalePrice1'])
    skew_GrLivArea = skew(data['GrLivArea1'])
    return skew_GrLivArea,skew_SalePrice

print skewness_log(data)
