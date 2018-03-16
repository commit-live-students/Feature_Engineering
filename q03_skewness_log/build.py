# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:

def skewness_log(data):
#     for col in ['GrLivArea','SalePrice']:
#         data[col] = data[col].fillna(data[col].mean())
    
#     print(skew(data['GrLivArea']))
#     print(skew(data['SalePrice']))
    
    data['GrLivArea'] = np.log(data['GrLivArea'])
    data['SalePrice'] = np.log(data['SalePrice'])
    
    skewness1 = skew(data['GrLivArea'])
    skewness2 = skew(data['SalePrice'])
    
    return skewness1, skewness2

    
    
    
#skewness_log(data)    
    


