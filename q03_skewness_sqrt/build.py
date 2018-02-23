# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['SalePrice'] = np.sqrt(data['SalePrice'])
    skewness_sale = skew(data['SalePrice'])

    data['GrLivArea'] = np.sqrt(data['GrLivArea'])
    skewness_gr = skew(data['GrLivArea'])

    return skewness_gr, skewness_sale
