# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    s1=np.sqrt(data['GrLivArea'])
    skw1=skew(s1)
    s2=np.sqrt(data['SalePrice'])
    skw2=skew(s2)
    return skw1,skw2



