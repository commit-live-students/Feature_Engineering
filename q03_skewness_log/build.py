# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data.loc[:,'SalePrice1'] =data['SalePrice']
    data.loc[:,'GrLivArea1'] =data['GrLivArea']
    data['SalePrice1']=np.log(data['SalePrice1'])
    data['GrLivArea1']=np.log(data['GrLivArea1'])
    skew1=skew(data['SalePrice1'])
    skew2=skew(data['GrLivArea1'])
    return skew2,skew1


