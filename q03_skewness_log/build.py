# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log(data):
    
    df = data.copy()
    df['GrLivArea'] = np.log(df['GrLivArea'])
    df['SalePrice'] = np.log(df['SalePrice'])
    
    skewed_grLiv = skew(df['GrLivArea'])
    skewed_SalePrice = skew(df['SalePrice'])
    
    return skewed_grLiv, skewed_SalePrice

skewness_log(data)



