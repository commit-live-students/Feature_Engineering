






# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal (dataset):
    target_column= 'SalePrice'
    df= dataset.copy()
    num_columns =df.select_dtypes(include=['float64','int64'])

    num_columns = num_columns.drop(target_column,1)
    #quantile_95= num_columns.quantile(0.9385)
    quantile_95= num_columns.quantile(0.95)

    for colname in num_columns:
        quantile =  quantile_95[ colname ]
        print colname, ":", quantile
        df=df.drop(df[df[colname]>quantile].index)

    return df

df = outlier_removal(housing_data)
print df.describe(include='all')
