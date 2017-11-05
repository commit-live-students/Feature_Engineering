# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
housing_data
def imputation(df):

    total = df.isnull().sum(axis=0).sort_values(ascending=False)
    percent = ((df.isnull().sum(axis=0)/df.isnull().count(axis=0))*100).sort_values(ascending=False)

    missing_data_columns = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    df2=df.copy()
    MasVnrAreaMean = df['MasVnrArea'].mean()

    imp1 = df2["GarageType"].fillna("None")
    imp2 = df2['MasVnrArea'].fillna(MasVnrAreaMean)
    imp1 = imp1.to_frame()
    imp2 = imp2.to_frame()

 #   df = df.to_frame().reset_index()
#      df2["GarageType"] = df2["GarageType"].fillna("None")
#     df2['MasVnrArea'] = df2['MasVnrArea'].fillna(MasVnrAreaMean)


    return imp1, imp2



#imputation(housing_data)
