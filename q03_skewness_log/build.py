from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    data_trans = data.copy()
    data_trans["SalePrice"] = np.log(data_trans["SalePrice"])
    data_trans["GrLivArea"] = np.log(data_trans["GrLivArea"])
    skew_sp = skew(data_trans["SalePrice"])
    skew_gla = skew(data_trans["GrLivArea"])
    return skew_gla, skew_sp
