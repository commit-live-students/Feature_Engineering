from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(df):
    data['SalePrice'] = np.log(data['SalePrice'])
    data['GrLivArea'] = np.log(data['GrLivArea'])

    skew_1 = skew(data['GrLivArea'])
    skew_2 = skew(data['SalePrice'])

    return skew_1, skew_2
