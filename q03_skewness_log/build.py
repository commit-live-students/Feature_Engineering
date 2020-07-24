# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

data = pd.read_csv('data/train.csv')
# Write code here:
def skewness_log(data):
    dataset = data.copy()
    #sns.distplot(dataset['GrLivArea'])
    #sns.distplot(dataset['SalePrice'])
    #fig = plt.figure()
    #stats.probplot(dataset['GrLivArea'],plot=plt)
    #stats.probplot(dataset['SalePrice'],plot=plt)
    #plt.show()

    #skewness_grLiv = skew(dataset['GrLivArea'])
    #skewness_spc = skew(dataset['SalePrice'])
    #print(skewness_grLiv)
    #print(skew(np.log(dataset['GrLivArea'])))
    #sns.distplot(np.log(dataset['GrLivArea']))
    #fig = plt.figure()
    #stats.probplot(np.log(dataset['GrLivArea']),plot=plt)
    #stats.probplot(np.log(dataset['SalePrice']),plot=plt)
    #plt.show()

    skewness_1 = skew(np.log(dataset['GrLivArea']))
    skewness_2 = skew(np.log(dataset['SalePrice']))

    return skewness_1,skewness_2

