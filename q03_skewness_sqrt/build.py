# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


def skewness_sqrt(my_housing):
    df = ny_housing[['GrLivArea','SalePrice']]

    df_trans=df.copy()
    df_trans['GrLivArea'] = np.sqrt(df_trans['GrLivArea'])
    df_trans['SalePrice'] = np.sqrt(df_trans['SalePrice'])

    skewness_grLiv = skew(df_trans['GrLivArea'])
    #print(skewness_grLiv)

    skewness_saleprc = skew(df_trans['SalePrice'])
    #print(skewness_saleprc)

    return skewness_grLiv, skewness_saleprc
