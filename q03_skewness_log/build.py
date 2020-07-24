# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np



data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(df):
    
    df['SalePrice_trans']=np.log(df['SalePrice'])
    df['GrLivArea_trans']=np.log(df['GrLivArea'])
    skew_SalePrice=skew(df['SalePrice_trans'])
    skew_GrLivArea=skew(df['GrLivArea_trans'])
    return(skew_GrLivArea,skew_SalePrice)
        
#skewness_log(data)


