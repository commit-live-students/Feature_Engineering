# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(ny_housing):
    
    ny_housing['SalePrice1']=np.sqrt(ny_housing['SalePrice'])
    skew_SalePrice1=skew(ny_housing['SalePrice1'])
    ny_housing['GrLivArea1']=np.sqrt(ny_housing['GrLivArea'])
    skew_GrLivArea1=skew(ny_housing['GrLivArea1'])
    return skew_GrLivArea1,skew_SalePrice1
    

skewness_sqrt(ny_housing)


