import pandas as pd 
pd.options.display.max_columns=200
import numpy
from sklearn.ensemble import RandomForestRegressor


df=pd.read_csv('chronic_kidney_disease_full.arff')
df=df.replace('\?',-1,regex=True)
df=df.replace('^present|^normal$|good|yes$|^ckd$|^ckd\t$',1,regex=True)
df=df.replace('poor|abnormal|notpresent|no$|notckd',0,regex=True)


n_estimators=150
regressor = RandomForestRegressor(n_estimators, min_samples_split=1)

data_slice=.9*len(df)
X_train=df.ix[:data_slice,:-1].astype(float)
X_test=df.ix[data_slice:,:-1].astype(float)
y_train=df.ix[:data_slice,-1]
y_test=df.ix[data_slice:-1]

regressor.fit(X_train, y_train)
prediction=regressor.predict(X_test)
print prediction
print len(prediction)
