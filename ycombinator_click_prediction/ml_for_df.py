import pandas as pd
import pickle
import numpy
from sklearn.ensemble import RandomForestRegressor

df = pd.read_pickle('numeric_df.pkl')
df=df.fillna(0)

n_estimators=150
regressor = RandomForestRegressor(n_estimators, min_samples_split=1)

data_slice=.9*len(df)
X_train=df.ix[:data_slice,:-4].astype(float)
X_test=df.ix[data_slice:,:-4].astype(float)
y_train=df.ix[:data_slice,-4:]
y_test=df.ix[data_slice:,-4:]

regressor.fit(X_train, y_train)
prediction=regressor.predict(X_test)
print prediction
print len(prediction)



