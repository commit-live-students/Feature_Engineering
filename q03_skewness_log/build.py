# %load q03_skewness_log/build.py
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns
from scipy import stats
#For some Statistics
from scipy.stats import norm, skew
from sklearn.preprocessing import Imputer

df = pd.read_csv('data/train.csv')

def skewness_log(df):
    
    df['GrLivArea'] = np.log(df['GrLivArea'])
    skewed_grLiv = skew(df['GrLivArea'])

    df['SalePrice'] = np.log(df['SalePrice'])
    skewed_grLiv1 = skew(df['SalePrice'])
    return skewed_grLiv, skewed_grLiv1

#skewness_log(df)

# Write code here:



