# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(data):

    sale = np.sqrt(data['SalePrice'])
    grLiv = np.sqrt(data['GrLivArea'])

    skewed_sale = skew(sale)
    skewed_grLiv = skew(grLiv)

    return skewed_grLiv, skewed_sale
