# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(ny_housing):
    ny_housing['GrLivArea'] = np.sqrt(ny_housing['GrLivArea'])
    ny_housing['SalePrice'] = np.sqrt(ny_housing['SalePrice'])
    skewed_grLiv = skew(ny_housing['GrLivArea'])
    skewed_Sale = skew(ny_housing['SalePrice'])
    return skewed_grLiv, skewed_Sale

skewness_sqrt(ny_housing)


