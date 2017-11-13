from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


def skewness_log(data):
    data['SalePrice'] = np.sqrt(data['SalePrice'])
    data['GrLivArea'] = np.sqrt(data['GrLivArea'])

    skew_1 = skew(data['GrLivArea'])
    skew_2 = skew(data['SalePrice'])

    return skew_1, skew_2
