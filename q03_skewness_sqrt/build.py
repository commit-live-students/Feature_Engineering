# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(ny_housing):
    df_trans = ny_housing.copy()
    df_trans['SalePrice'] = np.sqrt(df_trans['SalePrice'])
    skewness_SalePrice  = skew(df_trans['SalePrice'])
    #print(skewness_SalePrice)

    df_trans['GrLivArea'] = np.sqrt(df_trans['GrLivArea'])
    skewness_GrLivArea  = skew(df_trans['GrLivArea'])
   #print(skewness_GrLivArea)

    return skewness_GrLivArea,skewness_SalePrice



# Write your Solution Here:
