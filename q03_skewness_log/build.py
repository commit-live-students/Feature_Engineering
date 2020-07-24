# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')
def skewness_log(data):
    skew1 = np.log(data.GrLivArea)
    skew1 = skew(skew1)
    skew2 = np.log(data.SalePrice)
    skew2 = skew(skew2)
    return skew1, skew2


