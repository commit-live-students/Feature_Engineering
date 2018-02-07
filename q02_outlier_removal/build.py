# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
# def outlier_removal(housing_data):
#     a = housing_data[['MasVnrArea', 'GrLivArea', 'SalePrice']].quantile(0.05)
#     b = housing_data[['MasVnrArea', 'GrLivArea', 'SalePrice']].quantile(0.95)
#     print(a, b)
#     housing_data = housing_data.drop(housing_data[(housing_data['MasVnrArea'] > 460)].index)
#     housing_data = housing_data.drop(housing_data[(housing_data['GrLivArea'] > 2500)].index)
#     housing_data = housing_data.drop(housing_data[(housing_data['SalePrice'] > 326100)].index)
#     housing_data[''] = range(len(housing_data))
#     housing_data.set_index('', inplace=True)
#     return housing_data
def outlier_removal (dataset):
    df= dataset.copy()
    num_columns =df.select_dtypes(include=['float64','int64'])


    quantile_95= num_columns.quantile(0.95)

    for colname in num_columns:
        quantile = quantile_95[ colname ]
        print quantile
        df=df.drop(df[df[colname]>quantile].index)


    return df
