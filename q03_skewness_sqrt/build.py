# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    
    sal_sqrt = np.sqrt(ny_housing.SalePrice)
    gr_sqrt = np.sqrt(ny_housing.GrLivArea)
    
    return skew(gr_sqrt), skew(sal_sqrt)
skewness_sqrt(ny_housing)


