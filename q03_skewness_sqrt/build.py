# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')
# Write your Solution Here:

dataset = ny_housing.copy()
def skewness_sqrt(dataset):
    skewness_gla = skew(dataset['GrLivArea'])
    print('GrLivArea Skewness :',skewness_gla)
    skewness_gla = skew(np.sqrt(dataset['GrLivArea']))
    print('GrLivArea Skewness after sqrt :',skewness_gla)

    skewness_spc = skew(dataset['SalePrice'])
    print('GrLivArea SalePrice :',skewness_spc)
    skewness_spc = skew(np.sqrt(dataset['SalePrice']))
    print('GrLivArea SalePrice after sqrt :',skewness_spc)

    return skewness_gla,skewness_spc


