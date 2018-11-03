# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(df):
    qv = 0.95
    df_qv = df.quantile(q=qv, axis=0, numeric_only=True, interpolation='linear')
    numeric_features = [a for a in range(len(df.dtypes)) if df.dtypes[a] in ['int64','float64']]
    numeric_df = df.iloc[:, numeric_features]
    for feature in numeric_df.columns:
        df=df.drop(df[df[feature]>df_qv[feature]].index)
    return df





