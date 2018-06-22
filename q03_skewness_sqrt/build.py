# %load q03_skewness_sqrt/build.py
# Default imports
from scipy import stats
from scipy.stats import skew,norm
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
ny_housing = pd.read_csv('data/train.csv')
# Write your Solution Here:
def skewness_sqrt(ny_housing):
    ny_housing['GrLivAreaST'] = np.sqrt(ny_housing['GrLivArea'])
    skewness_grLiv = skew(ny_housing['GrLivAreaST'])
    ny_housing['SalePriceST'] = np.sqrt(ny_housing['SalePrice'])
    skewness_SalePrc = skew(ny_housing['SalePriceST'])
    return skewness_grLiv,skewness_SalePrc



