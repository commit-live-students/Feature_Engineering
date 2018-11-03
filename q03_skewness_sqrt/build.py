# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(ny_housing):
    df = ny_housing.copy()
    df['GrLivArea'] = np.sqrt(df['GrLivArea'])
    df['SalePrice'] = np.sqrt(df['SalePrice'])
    
    skewed_grLiv = skew(df['GrLivArea'])
    skewed_SalePrice = skew(df['SalePrice'])
    
    return skewed_grLiv, skewed_SalePrice

skewness_sqrt(ny_housing)



