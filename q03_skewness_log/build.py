from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

# Write code here:
def skewness_log(df):
    skewed_grLiv = skew(df['GrLivArea'])
    #print(skewed_grLiv)
    df['GrLivArea'] = np.log(df['GrLivArea'])
    skewed_grLiv = skew(df['GrLivArea'])
    skewed_salePrice = skew(df['SalePrice'])
    #print(skewed_grLiv)
    #print(skewed_salePrice)
    df['SalePrice'] = np.log(df['SalePrice'])
    skewed_salePrice = skew(df['SalePrice'])
    #print(skewed_salePrice)

    return skewed_grLiv,skewed_salePrice

# Write code here:
