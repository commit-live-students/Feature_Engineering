# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def imputation(dataset):
    df = dataset

    numeric_feature = [a for a in range(len(df.dtypes)) if df.dtypes[a] in ['int64','float64']]
    numeric_data = df.iloc[:,numeric_feature]
    print numeric_data.head()

    for c in list(numeric_data):
        imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
        imp_mean.fit(numeric_data[[c]])
        numeric_data[c] = imp_mean.transform(numeric_data[[c]])

    cat_name = df.columns.difference(df.columns[numeric_feature])
    cat_data = df.loc[:,cat_name]

    for c in list(cat_data):
        cat_data[c]=cat_data[c].fillna(cat_data[c].mode()[0])
    return numeric_data , cat_data
