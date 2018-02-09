# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['SalePrice1'] = np.sqrt(data['SalePrice'])
    data['GrLivArea1'] = np.sqrt(data['GrLivArea'])
    skew_SalePrice = skew(data['SalePrice1'])
    skew_GrLivArea = skew(data['GrLivArea1'])
    return skew_GrLivArea,skew_SalePrice
