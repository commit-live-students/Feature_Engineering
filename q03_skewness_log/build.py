from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log(data):
    skewed_grLiv = skew(data['GrLivArea'])
    print(skewed_grLiv)
    data['GrLivArea'] = np.log(data['GrLivArea'])
    skw_trans_grliv=skew(data['GrLivArea'])


    skewed_salePrice = skew(data['SalePrice'])
    print(skewed_salePrice)
    data['SalePrice'] = np.log(data['SalePrice'])
    skw_trans_salePrice=skew(data['SalePrice'])

    return skw_trans_grliv,skw_trans_salePrice
print(skewness_log(data))
