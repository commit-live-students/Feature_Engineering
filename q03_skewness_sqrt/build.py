# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:

def skewness_sqrt(data):
    data['GrLivArea'] = np.sqrt(data['GrLivArea'])
    data['SalePrice'] = np.sqrt(data['SalePrice'])

    skewed_grLiv = skew(data['GrLivArea'])
    skewed_Sp = skew(data['SalePrice'])
    return skewed_grLiv,skewed_Sp
