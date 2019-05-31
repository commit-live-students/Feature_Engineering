# %load q03_skewness_log/build.py
from scipy.stats import skew, norm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    d = data.copy()
    d.GrLivArea = np.log(d.GrLivArea)
    grSkew = skew(d.GrLivArea)
    d.SalePrice = np.log(d.SalePrice)
    spSkew = skew(d.SalePrice)
    return grSkew, spSkew

skewness_log(data)


