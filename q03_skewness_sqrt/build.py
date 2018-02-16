# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')
def skewness_sqrt(df):
    sale = df['SalePrice']
    area = df['GrLivArea']

    sale = np.sqrt(sale)
    area = np.sqrt(area)

    return skew(area), skew(sale)

# Write your Solution Here:
