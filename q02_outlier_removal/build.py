# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def outlier_removal(dataset):
    numeric_feature = [a for a in range(len(housing_data.dtypes)) if housing_data.dtypes[a] in ['int64','float64']]
    numeric_data = housing_data.iloc[:,numeric_feature]

    cat_name = housing_data.columns.difference(housing_data.columns[numeric_feature])
    cat_data = housing_data.loc[:,cat_name]
    fill_Nan = Imputer(missing_values=np.nan, strategy='mean',axis=1)
    imputed_DF_numeric = pd.DataFrame(fill_Nan.fit_transform(numeric_data))
    imputed_DF_numeric.columns = numeric_data.columns
    imputed_DF_numeric.index = numeric_data.index
    for a in cat_data:
        cat_data.loc[:,a]=cat_data.loc[:,a].fillna(cat_data.loc[:,a].mode()[0])
    imputed_housing_data=pd.concat([imputed_DF_numeric,cat_data],axis=1)
    a=imputed_housing_data.quantile(0.95,axis=0)
    new_df=imputed_housing_data[a.index]<a
    return new_df.any(axis=1)
