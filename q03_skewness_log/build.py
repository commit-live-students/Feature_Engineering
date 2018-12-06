# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data['GrLivAreaLT'] = np.log(data['GrLivArea'])
    skewed_grLiv = skew(data['GrLivAreaLT'])
    
    data['SalePriceLT'] = np.log(data['SalePrice'])
    skewed_SaleP = skew(data['SalePriceLT'])
    
    return skewed_grLiv, skewed_SaleP
    

