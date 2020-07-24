# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:

def skewness_sqrt(ny_housing):
    skewed_sqrt_val2 = skew(np.sqrt(ny_housing['SalePrice']))
    skewed_sqrt_val1 = skew(np.sqrt(ny_housing['GrLivArea']))
    return skewed_sqrt_val1,skewed_sqrt_val2

skewness_sqrt(ny_housing)



