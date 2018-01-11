# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

# Write your Solution Here:
def skewness_sqrt(df) :
    skewGr1 = skew(df['GrLivArea'])
#     print('Before :',skewGr1)

    df_trans=df.copy()
    df_trans['GrLivArea'] = np.sqrt(df_trans['GrLivArea'])
    skewGr2 = skew(df_trans['GrLivArea'])
#     print('After :',skewGr2)

    skewSale1 = skew(df['SalePrice'])
#     print('Before :',skewSale1)
    df_trans['SalePrice'] = np.sqrt(df_trans['SalePrice'])
    skewSale2 = skew(df_trans['SalePrice'])
#     print('After :',skewSale2)
    return skewGr2,skewSale2
# skewness_sqrt(ny_housing)
