from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(df):
    skew_ga=skew(np.log(df.GrLivArea))
    skew_sp=skew(np.log(df.SalePrice))
    return skew_ga,skew_sp
