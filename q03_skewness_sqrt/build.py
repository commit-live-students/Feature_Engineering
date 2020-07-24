# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['GrLivAreaLT'] = np.sqrt(data['GrLivArea'])
    skewed_grLiv = skew(data['GrLivAreaLT'])
    
    data['SalePriceLT'] = np.sqrt(data['SalePrice'])
    skewed_SaleP = skew(data['SalePriceLT'])
    
    return skewed_grLiv, skewed_SaleP

# skewness_sqrt(ny_housing)


