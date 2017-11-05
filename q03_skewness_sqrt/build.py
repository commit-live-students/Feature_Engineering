# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


def skewness_sqrt(df):
    df_trans = df.copy()
    df_trans['GrLivArea'] = np.sqrt(df_trans['GrLivArea'])
    skewness_GrLivArea = skew(df_trans['GrLivArea'])

    df_trans['SalePrice'] = np.sqrt(df_trans['SalePrice'])
    skewness_saleprice = skew(df_trans['SalePrice'])
    return skewness_GrLivArea, skewness_saleprice
