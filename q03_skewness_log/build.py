from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


def skewness_log(df):
    df_transposed = df.copy()
    df_transposed['SalePrice'] = np.log(df_transposed['SalePrice'])
    df_transposed['GrLivArea'] = np.log(df_transposed['GrLivArea'])
    skew_sp = skew(df_transposed['SalePrice'])
    skew_gla = skew(df_transposed['GrLivArea'])
    return skew_gla,skew_sp
