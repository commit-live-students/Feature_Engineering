# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(df):
    numeric_features = [a for a in range(len(df.dtypes)) if df.dtypes[a] in ['int64','float64']]
    numeric_df = df.iloc[:, numeric_features]
    cat_features = df.columns.difference(df.columns[numeric_features])
    cat_df = df.loc[:,cat_features]
    numeric_imputer = Imputer(missing_values = 'NaN', strategy='mean')
    numeric_imputed_df = pd.DataFrame(numeric_imputer.fit_transform(numeric_df))
    numeric_imputed_df.columns = numeric_df.columns
    numeric_imputed_df.index = numeric_df.index
    for feature in cat_features:
        cat_df[feature] = cat_df[feature].fillna(cat_df[feature].mode()[0])
    return numeric_imputed_df, cat_df




