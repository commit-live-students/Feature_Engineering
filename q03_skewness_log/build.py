# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

# Write code here:

def skewness_log(data):
    target1 = np.log(data['SalePrice'])
    sk_val1 = skew(target1)
 
    target2 = np.log(data['GrLivArea'])
    sk_val2 = skew(target2)
    
    print (sk_val1,sk_val2)
    
    return sk_val2,sk_val1

skewness_log(data)





