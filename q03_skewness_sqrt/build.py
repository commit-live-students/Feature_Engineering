# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['sqrt_SalePrice']=np.sqrt(data['SalePrice'])
    data['sqrt_GrLivArea']=np.sqrt(data['GrLivArea'])
        
    return skew(data['sqrt_GrLivArea']),skew(data['sqrt_SalePrice'])


#Call to the function
skewness_sqrt(ny_housing)

