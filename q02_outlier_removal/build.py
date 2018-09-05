import pandas as pd
import numpy as np
 # Data
df = pd.read_csv('data/train.csv')

def outlier_removal(df):
    df=df.drop(df[(df['GrLivArea']>df['GrLivArea'].quantile(0.95)) | (df['MasVnrArea']>df['MasVnrArea'].quantile(0.95)) | (df['SalePrice']>df['SalePrice'].quantile(0.95))].index)
    return (df)



