# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:

def skewness_sqrt(data):
    data['GrLivAreaSqrt'] = np.sqrt(data['GrLivArea'])
    data['SalePriceSqrt'] = np.sqrt(data['SalePrice'])
    return skew(data.GrLivAreaSqrt), skew(data.SalePriceSqrt)
