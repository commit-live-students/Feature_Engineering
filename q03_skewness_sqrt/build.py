# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(ny_housing):
    skewness_SpLiv1 = skew(ny_housing['SalePrice'])
    skewness_grLiv1 = skew(ny_housing['GrLivArea'])
    ny_housing['SalePrice'] = np.sqrt(ny_housing['SalePrice'])
    ny_housing['GrLivArea'] = np.sqrt(ny_housing['GrLivArea'])
    skewness_SpLiv2 = skew(ny_housing['SalePrice'])
    skewness_grLiv2 = skew(ny_housing['GrLivArea'])
    return skewness_grLiv2,skewness_SpLiv2

skewness_sqrt(ny_housing)

