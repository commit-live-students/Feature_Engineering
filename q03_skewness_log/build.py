from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(df) :
    skewGr1 = skew(df['GrLivArea'])
#     print df['GrLivArea']
#     print('Before :',skewGr1)

    df_trans=df.copy()
    df_trans['GrLivArea'] = np.log(df_trans['GrLivArea'])
#     print df_trans['GrLivArea']
    skewGr2 = skew(df_trans['GrLivArea'])
#     print('After :',skewGr2)

    skewSale1 = skew(df['SalePrice'])
#     print('Before :',skewSale1)
    df_trans['SalePrice'] = np.log(df_trans['SalePrice'])
    skewSale2 = skew(df_trans['SalePrice'])
#     print('After :',skewSale2)
    return skewGr2,skewSale2
# skewness_log(data)
