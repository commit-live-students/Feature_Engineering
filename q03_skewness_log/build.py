from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def rf_rfe(df):
    model = RandomForestClassifier()
    X, y = data.iloc[:,:-1], data.iloc[:,-1]
    nf= X.shape[1]/2
    rfe = RFE(model, n_features_to_select=nf)
    rfe = rfe.fit(X, y)
    lst = [];
    for i,rank in enumerate(rfe.ranking_):
        if(rank==1):
            lst.append(X.columns[i])

    return lst
