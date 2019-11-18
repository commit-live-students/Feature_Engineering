# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/train.csv')


def skewness_log(data):
    data['GrLivArea'] = np.log(data['GrLivArea'])
    data['SalePrice'] = np.log(data['SalePrice'])
    skew_GrLivArea = skew(data['GrLivArea'])
    skew_SalePrice = skew(data['SalePrice'])
    return skew_GrLivArea, skew_SalePrice
    

