# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    data_trans = data.copy()
    data_trans["SalePrice"] = np.sqrt(data_trans["SalePrice"])
    data_trans["GrLivArea"] = np.sqrt(data_trans["GrLivArea"])
    skew_sp = skew(data_trans["SalePrice"])
    skew_gla = skew(data_trans["GrLivArea"])
    return skew_gla, skew_sp
