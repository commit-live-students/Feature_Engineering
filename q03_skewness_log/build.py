from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log(data):
    df_trans=data.copy()
    df_trans['SalePrice'] = np.log(df_trans['SalePrice'])
    skewness_SalePrice = skew(df_trans['SalePrice'])
    #print(skewness_SalePrice)

    df_trans['GrLivArea'] = np.log(df_trans['GrLivArea'])
    skewness_GrLivArea = skew(df_trans['GrLivArea'])
   #print(skewness_GrLivArea)
    #skewed_grLiv = skew(df['SalePrice'])
   # print(skewed_grLiv)

    return skewness_GrLivArea,skewness_SalePrice


# Write code here:
