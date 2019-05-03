from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


def skewness_log(data):
    df = data[['GrLivArea','SalePrice']]

    df_trans=df.copy()
    df_trans['GrLivArea'] = np.log(df_trans['GrLivArea'])
    df_trans['SalePrice'] = np.log(df_trans['SalePrice'])

    skewness_grLiv = skew(df_trans['GrLivArea'])
    print(skewness_grLiv)

    skewness_saleprc = skew(df_trans['SalePrice'])
    print(skewness_saleprc)

    return skewness_grLiv, skewness_saleprc
