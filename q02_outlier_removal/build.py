# Default imports
import pandas as pd
from pandas import DataFrame

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(data):

    df = data.copy()

    for col in ('MasVnrArea', 'GrLivArea', 'SalePrice'):
        df[col] = df[col].fillna(df[col].mean())

    quantile_value = df.quantile(0.95)
    index = quantile_value.index.values

    df = df[df[index[0]] <= quantile_value[0]]
    df = df[df[index[1]] <= quantile_value[1]]
    df = df[df[index[2]] <= quantile_value[2]]

    # filt_df = pd.concat([df.loc[:,'LotShape'], filt_df], axis=1)
    #df = df.apply(lambda x: x[(x < quantile_value.loc[x.name])], axis=0)

    return df
