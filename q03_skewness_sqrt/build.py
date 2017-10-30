# %load q03_skewness_log/build.py
from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

def skewness_sqrt(data):
    sk_saleprice=skew(np.sqrt(data['SalePrice']))
    sk_GrLivArea=skew(np.sqrt(data['GrLivArea']))
#df_trans['Log_Gl_Area']=np.log(df_trans['GrLivArea'])
    return sk_GrLivArea,sk_saleprice
