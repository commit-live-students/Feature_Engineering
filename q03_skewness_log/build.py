from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:

def skewness_log(data):
    data['GrLivArea'] = np.log(data['GrLivArea'])
    data['SalePrice'] = np.log(data['SalePrice'])

    skewed_grLiv = skew(data['GrLivArea'])
    skewed_Sp = skew(data['SalePrice'])
    return skewed_grLiv,skewed_Sp
