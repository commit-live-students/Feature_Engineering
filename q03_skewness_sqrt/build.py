# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['SalePrice'] = np.sqrt(data['SalePrice'])
    data['GrLivArea'] = np.sqrt(data['GrLivArea'])

    skew_1 = skew(data['GrLivArea'])
    skew_2 = skew(data['SalePrice'])

    return skew_1, skew_2
