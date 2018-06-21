# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(ny_housing):
    
     return(skew(np.sqrt(ny_housing['GrLivArea'])),skew(np.sqrt(ny_housing['SalePrice'])))

# Write your Solution Here:



