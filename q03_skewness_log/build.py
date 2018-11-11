# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    GrlivArea_array = np.array(data['GrLivArea'])
    SalePrice_array = np.array(data['SalePrice'])
    
    GrLivArea95 = np.percentile(GrlivArea_array,0.95)
    SalePrice95 = np.percentile(SalePrice_array,0.95)
    
    return skew(np.log(GrlivArea_array)),skew(np.log(SalePrice_array))













