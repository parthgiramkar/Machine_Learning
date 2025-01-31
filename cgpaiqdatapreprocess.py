import numpy as np
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/placement.csv')

df= df.iloc[ : , 1 : ]                                  #it preprocessed the data by removing col named-unnnanmed try it to find that prev col

df.head()

df.shape

import matplotlib.pyplot as plt

plt.scatter(df ["cgpa"] ,df ["iq"])

#in colour form

plt.scatter(df ["cgpa"] ,df ["iq"] , c=df["placement"])

#linear regression - EDA
#feature scaling
X= df.iloc[ : ,0:2]
y=df.iloc[ : ,-1]

X

y

y.shape
#1-D tensor

#Train test split
# cgpa and iq i.e - X are independent variables as no link to each other and y dependent variable we have to give
# test_size=0.1-- 10% of 100 to testing and later to training
from sklearn.model_selection import train_test_split
train_test_split( X , y ,test_size=0.1)

X_train, X_test ,y_train ,y_test = train_test_split( X , y ,test_size=0.1)

X_train

X_test

y_test

#scaling

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()               #created obj scaler

X_train = scaler.fit_transform(X_train)

X_train

from sklearn.linear_model import LogisticRegression
clf= LogisticRegression()               #created obj of clf

#Model training of trained model
clf.fit(X_train , y_train)

y_pred=clf.predict(X_test)

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_test , y_pred)

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(X_train , y_train.values , clf=clf , legend=2)

import pickle

pickle.dump(clf, open('model.pkl' , 'wb') )
