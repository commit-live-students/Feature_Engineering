# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    
    sal_log = np.log(data.SalePrice)
    Gr_log = np.log(data.GrLivArea)
    
    return skew(Gr_log), skew(sal_log)
skewness_log(data)



