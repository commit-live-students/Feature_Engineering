# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(ny_housing):
    skew1 = np.sqrt(ny_housing.SalePrice)
    skew1 = skew(skew1)
    skew2 = np.sqrt(ny_housing.GrLivArea)
    skew2 = skew(skew2)
    return skew2, skew1

skewness_sqrt(ny_housing)

