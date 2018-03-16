# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
#     for col in ['GrLivArea','SalePrice']:
#         data[col] = data[col].fillna(data[col].mean())
    
#     print(skew(data['GrLivArea']))
#     print(skew(data['SalePrice']))
    
    data['GrLivArea'] = np.sqrt(data['GrLivArea'])
    data['SalePrice'] = np.sqrt(data['SalePrice'])
    
    skewness1 = skew(data['GrLivArea'])
    skewness2 = skew(data['SalePrice'])
    
    return skewness1, skewness2

#skewness_sqrt(ny_housing)

