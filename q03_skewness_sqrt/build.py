# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(df):
    skew_var = ['GrLivArea', 'SalePrice']
    ret = []
    for colName in skew_var:
        df[colName] = np.sqrt(df[colName])
        ret.append(skew(df[colName]))
    return ret[0], ret[1]

# print "#### Testint ####"
# a, b = skewness_sqrt(ny_housing)
# print a, b
# print type(a), type(b)
