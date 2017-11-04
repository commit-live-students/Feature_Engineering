# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(df):
    df_transposed = df.copy()
    df_transposed['SalePrice'] = np.sqrt(df_transposed['SalePrice'])
    df_transposed['GrLivArea'] = np.sqrt(df_transposed['GrLivArea'])
    skew_sp = skew(df_transposed['SalePrice'])
    skew_gla = skew(df_transposed['GrLivArea'])
    return skew_gla,skew_sp
