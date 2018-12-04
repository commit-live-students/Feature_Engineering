# %load q01_missing_value/build.py
# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]



# Write your code here:
def imputation(dataset):
    
    #housing_data.isnull().sum(axis=0)  Gives missing values count before imputing values.
    all_columns = dataset.columns
    numeric_columns = dataset._get_numeric_data().columns
    categoric_columns = list(set(all_columns)-set(numeric_columns))

    for num_col in numeric_columns:
        dataset[num_col].fillna(dataset[num_col].mean(),inplace=True)


    for cat_col in categoric_columns:
        dataset[cat_col].fillna(dataset[cat_col].mode()[0],inplace=True)
    
    #housing_data.isnull().sum(axis=0)  Gives missing values count post imputing values.
    return pd.DataFrame(dataset[numeric_columns]),pd.DataFrame(dataset[categoric_columns])


#Call to the function 
x,y = imputation(housing_data)
y



