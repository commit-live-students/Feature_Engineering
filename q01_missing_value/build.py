# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
df = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

#housing_data.info()

def imputation(df):
    #missing data observing in columns
    df["GarageType"] = df["GarageType"].fillna("None")

    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(df[['MasVnrArea']])
    df['MasVnrArea'] = imp_mean.transform(df[['MasVnrArea']])

    """total = df.isnull().sum(axis=0).sort_values(ascending=False)
    percent = ((df.isnull().sum(axis=0)/df.isnull().count(axis=0))*100).sort_values(ascending=False)

    # count the number of null values in the column and their perecentage of the total data
    missing_data_columns = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    missing_data_columns.head(20)"""
    return pd.DataFrame(df['MasVnrArea']), pd.DataFrame(df['GarageType'])

imputation(df)
#df['GarageType'].isnull().values.any()
