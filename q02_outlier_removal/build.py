# Default imports
import pandas as pd
from pandas import DataFrame

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(data):

    df = data.copy()
    #my code

    # # for col in ('MasVnrArea', 'GrLivArea', 'SalePrice'):
    # #     df[col] = df[col].fillna(df[col].mean())
    #
    # quantile_value = df.quantile(0.95, axis = 0)
    # print(quantile_value[0])
    #
    # index = quantile_value.index.values
    #
    # df = df[df[index[0]] <= quantile_value[0]]
    # df = df[df[index[1]] <= quantile_value[1]]
    # df = df[df[index[2]] <= quantile_value[2]]

    ####df = df.apply(lambda x: x[(x < quantile_value.loc[x.name])], axis=0)

    ## 2nd code

    q = df.quantile(0.95, axis = 0)

    df = df.drop(df[df.MasVnrArea > q[0]].index)
    df = df.drop(df[df.GrLivArea > q[1]].index)
    df = df.drop(df[df.SalePrice > q[2]].index)

    return df
