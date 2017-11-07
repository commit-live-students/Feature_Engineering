from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:

def skewness_log(data):
    data['GrLivAreaLog'] = np.log(data['GrLivArea'])
    data['SalePriceLog'] = np.log(data.SalePrice)
    return skew(data.GrLivAreaLog),skew(data.SalePriceLog)
