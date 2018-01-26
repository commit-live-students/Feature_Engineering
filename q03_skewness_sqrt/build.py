# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    df_trans=data.copy()
    df_trans['new_GrLivArea'] = np.sqrt(df_trans['GrLivArea'])
    skewness_grLiv = skew(df_trans['new_GrLivArea'])
    df_trans['new_SalePrice'] = np.sqrt(df_trans['SalePrice'])
    skewness_sale = skew(df_trans['new_SalePrice'])
    return skewness_grLiv,skewness_sale
