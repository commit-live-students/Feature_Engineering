# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('data/train.csv')



def skewness_log(data):
    
    data['SalePrice']=np.log(data['SalePrice'])
    data['GrLivArea']=np.log(data['GrLivArea'])
    return skew(data['GrLivArea']),skew(data['SalePrice'])




