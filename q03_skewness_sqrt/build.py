# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(df):
    skew_ga=skew(np.sqrt(df.GrLivArea))
    skew_sp=skew(np.sqrt(df.SalePrice))
    return skew_ga,skew_sp
