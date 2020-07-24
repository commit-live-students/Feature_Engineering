# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):

    #Dropping Null value rows
    dataset = dataset.dropna()
    
    #Variable to store quantile value
    Target_95_quantile = dataset.iloc[:,-1].quantile(0.95)

    #Taking values less than or equal to 95th quantile cutoff for SalePrice. 
    #i.e. indirectly filtering out values greater than o.95 quantile
    dataset=dataset[dataset.iloc[:,-1]<=Target_95_quantile]
        
    return dataset
 

#Call to the function
outlier_removal(housing_data)



