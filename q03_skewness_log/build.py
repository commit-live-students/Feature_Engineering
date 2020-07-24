# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    return skew(np.log(data['GrLivArea'])), skew(np.log(data['SalePrice']))

skewness_log(data)


