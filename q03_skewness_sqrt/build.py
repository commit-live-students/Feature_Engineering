# %load q03_skewness_sqrt/build.py
# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')


# Write your Solution Here:
def skewness_sqrt(data):
    #skewed_grLiv = skew(data['GrLivArea'])
    #print(skewed_grLiv)
    # puttinglog
    df_trans= data.copy()
    df_trans['GrLivArea']=np.sqrt(df_trans['GrLivArea'])
    df_trans['SalePrice']=np.sqrt(df_trans['SalePrice'])

    sk1=skew(df_trans['GrLivArea'])
    sk2=skew(df_trans['SalePrice'])
    return sk1,sk2

# sk1,sk2=skewness_sqrt(ny_housing)
# print(type(sk1),type(sk2))
# print(sk1,sk2)
