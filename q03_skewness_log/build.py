# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    skew1 = skew(np.log(data['GrLivArea']))
    skew2 = skew(np.log(data['SalePrice']))
    return skew1,skew2

