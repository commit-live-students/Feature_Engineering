# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data['SalePrice_trans']=np.sqrt(data['SalePrice'])
    data['GrLivArea_trans']=np.sqrt(data['GrLivArea'])
    skew_SalePrice=skew(data['SalePrice_trans'])
    skew_GrLivArea=skew(data['GrLivArea_trans'])
    return(skew_GrLivArea,skew_SalePrice)
        
#skewness_sqrt(ny_housing)


