import pandas as pd
import pickle
import numpy
from sklearn.ensemble import RandomForestRegressor

df = pd.read_pickle('numeric_df.pkl')
df=df.fillna(0)

n_estimators=150
regressor = RandomForestRegressor(n_estimators, min_samples_split=1)

# df = [           *            ]       ^
#      [           *            ]       |
#      [  x_train  *  y_train   ]   training_row_count
#      [           *            ]       |
#      [           *            ]       v
#      [************************]
#      [           *            ]
#      [  x_test   *   y_test   ]
#      [           *            ]
#
#                   <--- 4 ---->
#

training_row_count=int(.9*len(df))
y_column_count=4
X_train=df.ix[:training_row_count,:-1*y_column_count].astype(float)
X_test=df.ix[training_row_count:,:-1*y_column_count].astype(float)
y_train=df.ix[:training_row_count,-1*y_column_count:]
y_test=df.ix[training_row_count:,-1*y_column_count:]

regressor.fit(X_train, y_train)
prediction=regressor.predict(X_test)
print prediction
print len(prediction)



