# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew, norm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    d = data.copy()
    d.GrLivArea = np.sqrt(d.GrLivArea)
    grSkew = skew(d.GrLivArea)
    d.SalePrice = np.sqrt(d.SalePrice)
    spSkew = skew(d.SalePrice)
    return grSkew, spSkew

skewness_sqrt(ny_housing)


