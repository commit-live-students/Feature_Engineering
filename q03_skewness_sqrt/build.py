# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(df):
    df.loc[:,'SalePrice1'] =df['SalePrice']
    df.loc[:,'GrLivArea1'] =df['GrLivArea']
    df['SalePrice1']=np.sqrt(df['SalePrice1'])
    df['GrLivArea1']=np.sqrt(df['GrLivArea1'])
    skew1=skew(df['SalePrice1'])
    skew2=skew(df['GrLivArea1'])
    return skew2,skew1



