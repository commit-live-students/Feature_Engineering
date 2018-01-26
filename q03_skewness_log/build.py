from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    df_trans=data.copy()
    df_trans['new_GrLivArea'] = np.log(df_trans['GrLivArea'])
    skewness_grLiv = skew(df_trans['new_GrLivArea'])
    df_trans['new_SalePrice'] = np.log(df_trans['SalePrice'])
    skewness_sale = skew(df_trans['new_SalePrice'])
    return skewness_grLiv,skewness_sale
