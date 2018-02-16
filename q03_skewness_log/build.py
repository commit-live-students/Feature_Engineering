from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')
def skewness_log(df):
    sale = df['SalePrice']
    area = df['GrLivArea']

    sale = np.log(sale)
    area = np.log(area)

    return skew(area), skew(sale)

# Write code here:
