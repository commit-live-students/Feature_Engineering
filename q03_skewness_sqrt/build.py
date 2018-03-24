
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here :

def skewness_sqrt(data):
    data['GrLivArea2'] = np.sqrt(data['GrLivArea'])
    data['SalePrice2'] = np.sqrt(data['SalePrice'])
    skewed_GrLivArea2 = skew(data['GrLivArea2'])
    skewed_SalePrice2 = skew(data['SalePrice2'])
    return skewed_GrLivArea2, skewed_SalePrice2

