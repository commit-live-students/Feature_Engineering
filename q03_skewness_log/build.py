from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log (data):
    data['GrLivArea_1']=np.log(data['GrLivArea'])
    data['SalePrice_1']=np.log(data['SalePrice'])
    return (skew(data['GrLivArea_1']),skew(data['SalePrice_1']))

print skewness_log(data)
