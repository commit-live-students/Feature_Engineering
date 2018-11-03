import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(housing_data):
    df = housing_data
    qlt = housing_data.quantile(q=0.95)
    
    df = df.drop(df[(df['MasVnrArea']>qlt[0])].index)
    df = df.drop(df[(df['GrLivArea']>qlt[1])].index)
    df = df.drop(df[(df['SalePrice']>qlt[2])].index)
    
    return df

outlier_removal(housing_data)



