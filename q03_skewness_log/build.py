# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(df):
    skew_var = ['GrLivArea', 'SalePrice']
    ret = []
    for colName in skew_var:
        df[colName] = np.log(df[colName])
        ret.append(skew(df[colName]))
    return ret[0], ret[1]

print "#### Testint ####"
a, b = skewness_log(data)
print a, b
print type(a), type(b)
