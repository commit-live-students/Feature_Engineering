# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np
from math import sqrt

ny_housing = pd.read_csv('data/train.csv')

# Write your Solution Here:
def skewness_sqrt(ny_housing):
        
    target1 = np.sqrt(ny_housing['SalePrice'])
    sk_val1 = skew(target1)
 
    target2 = np.sqrt(ny_housing['GrLivArea'])
    sk_val2 = skew(target2)
    
    #print (sk_val2,sk_val1)
    
    return sk_val2,sk_val1

skewness_sqrt(ny_housing)



