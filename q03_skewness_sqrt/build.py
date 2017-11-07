# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np
from math import sqrt

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(ny_housing):
    ny_housing['GrLivArea1'] = np.sqrt(ny_housing['GrLivArea'])
    ny_housing['SalePrice1'] = np.sqrt(ny_housing['SalePrice'])
    skewed_sqrt_val1 = skew(ny_housing['GrLivArea1'])
    skewed_sqrt_val2 = skew(ny_housing['SalePrice1'])

    return skewed_sqrt_val1,skewed_sqrt_val2
