# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    s1=np.log(data['GrLivArea'])
    skw1=skew(s1)
    s2=np.log(data['SalePrice'])
    skw2=skew(s2)
    return skw1,skw2


