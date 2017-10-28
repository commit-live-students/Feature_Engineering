# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt (data):
    sp = np.sqrt(data['SalePrice'])
    val1 = skew(sp)
    gla = np.sqrt(data['GrLivArea'])
    val2 = skew(gla)
    return val2, val1


# Write your Solution Here:
