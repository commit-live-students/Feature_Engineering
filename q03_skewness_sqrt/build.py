# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    #df_trans = ny_housing.copy()
    data[['GrLivArea', 'SalePrice']] = np.sqrt(data[['GrLivArea', 'SalePrice']])
    skewed_grlives = skew(data['GrLivArea'])
    skewed_SalePrice = skew(data['SalePrice'])
    return skewed_grlives, skewed_SalePrice

#print skewness_sqrt(data=ny_housing)
