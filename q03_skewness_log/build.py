# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

# Write your Solution Here:
def skewness_log(data):
    #df_trans=data.copy()
    data[['GrLivArea', 'SalePrice']] = np.log(data[['GrLivArea', 'SalePrice']])
    skewed_grlivar = skew(data['GrLivArea'])
    skewed_saleprice = skew(data['SalePrice'])
    return skewed_grlivar, skewed_saleprice


print skewness_log(data = ny_housing)
