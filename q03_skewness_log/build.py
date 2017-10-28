from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log (data):
    sp = np.log(data['SalePrice'])
    val1 = skew(sp)
    gla = np.log(data['GrLivArea'])
    val2 = skew(gla)
    return val2, val1
# Write code here:
