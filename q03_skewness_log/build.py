from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


def skewness_log(data):

    sale = np.log(data['SalePrice'])
    grLiv = np.log(data['GrLivArea'])

    skewed_sale = skew(sale)
    skewed_grLiv = skew(grLiv)

    return skewed_grLiv, skewed_sale
