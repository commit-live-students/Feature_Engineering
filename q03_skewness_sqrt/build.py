# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:

def skewness_sqrt(df):
    logsaleprice = np.sqrt(df['SalePrice'])
    loggrlivarea = np.sqrt(df['GrLivArea'])
    
    skewsaleprice = skew(logsaleprice)
    skewgrlivarea = skew(loggrlivarea)
    
    return skewgrlivarea, skewsaleprice

skewness_sqrt(ny_housing)

