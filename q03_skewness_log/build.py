# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(df):
    logsaleprice = np.log(df['SalePrice'])
    loggrlivarea = np.log(df['GrLivArea'])
    
    skewsaleprice = skew(logsaleprice)
    skewgrlivarea = skew(loggrlivarea)
    
    return skewgrlivarea, skewsaleprice

skewness_log(data)

