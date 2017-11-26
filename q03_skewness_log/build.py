# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
df_trans=data.copy()



def skewness_log(data):
    data['GrLivArea1'] = np.log(data['GrLivArea'])
    data['SalePrice1'] = np.log(data['SalePrice'])
    skewed_val1 = skew(data['GrLivArea1'])
    skewed_val2 = skew(data['SalePrice1'])

    return skewed_val1,skewed_val2
