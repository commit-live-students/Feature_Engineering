# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt (data):
    data['GrLivArea_1']=np.sqrt(data['GrLivArea'])
    data['SalePrice_1']=np.sqrt(data['SalePrice'])
    return (skew(data['GrLivArea_1']),skew(data['SalePrice_1']))

#print skewness_sqrt(ny_housing)
