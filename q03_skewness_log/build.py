from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log(df):
    df['GrLivArea'] = np.log(df['GrLivArea'])
    df['SalePrice'] = np.log(df['SalePrice'])
    skewness_Sp = skew(df['SalePrice'])
    skewness_gl = skew(df['GrLivArea'])
    return skewness_gl,skewness_Sp
