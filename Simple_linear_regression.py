"""IMPORTING THE LIBRARIES"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""IMPORTING THE DATASET"""

dataframe = pd.read_csv('Salary_Data.csv')
x = dataframe.iloc[ : , : -1 ].values      #the rows and cols respectively as only two cols are there
y = dataframe.iloc[ : , : -1 ].values      #so exclude the last one

"""SPLITTING THE DATA INTO TRAINING _TEST AND TEST_SPLIT"""

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split( x , y , test_size = 0.2 , random_state = 1)

"""TRAINING THE SIMPLE LINEAR REGRESSION MODEL TO TRAINING SET"""

from sklearn.linear_model import LinearRegression
lr = LinearRegression()       # fit function of LinearRegression class
lr.fit( x_train , y_train)            #fit trains the training set i.e indep and dep variable
