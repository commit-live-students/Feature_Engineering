from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_log(data):
    #skewed_grLiv = skew(data['GrLivArea'])
    #print(skewed_grLiv)
    # puttinglog
    df_trans= data.copy()
    df_trans['GrLivArea']=np.log(df_trans['GrLivArea'])
    df_trans['SalePrice']=np.log(df_trans['SalePrice'])

    sk1=skew(df_trans['GrLivArea'])
    sk2=skew(df_trans['SalePrice'])
    return sk1,sk2

# sk1,sk2=skewness_log(data)
# print(type(sk1),type(sk2))
