# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    GrlivArea_array = np.array(data['GrLivArea'])
    SalePrice_array = np.array(data['SalePrice'])
    
    return skew(np.sqrt(GrlivArea_array)),skew(np.sqrt(SalePrice_array))


