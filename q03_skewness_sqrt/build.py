# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    return skew(np.sqrt(ny_housing['GrLivArea'])), skew(np.sqrt(ny_housing['SalePrice']))
