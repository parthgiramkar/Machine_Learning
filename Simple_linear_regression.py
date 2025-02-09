
Simple Linear Regression is used only when there is exactly one independent variable (feature) and one dependent variable (output). The output (
Y) should be a continuous numerical value. It should not be categorical (like "Yes" or "No").

"""IMPORTING THE LIBRARIES"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""IMPORTING THE DATASET"""

dataframe = pd.read_csv('Salary_Data.csv')
x = dataframe.iloc[ : , :-1 ].values      #the rows and cols respectively as only two cols are there
y = dataframe.iloc[ : , -1 ].values      #so include the last one

"""SPLITTING THE DATA INTO TRAINING _TEST AND TEST_SPLIT"""

from sklearn.model_selection import train_test_split      # 20% goes into the testing set
x_train , x_test , y_train , y_test = train_test_split( x , y , test_size = 0.2 , random_state = 0)

"""TRAINING THE SIMPLE LINEAR REGRESSION MODEL TO TRAINING SET"""

#APPLING the regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()       # fit function of LinearRegression class
lr.fit( x_train , y_train)            #fit trains the training set i.e indep and dep variable

"""PREDICTING THE TEST SET RESULTS"""

#fit() = Train the model requires input data (X) and target values (y)
#After fitting, we can use predict() to make prediction
y_pred = lr.predict(x_test)  #x_test contains the yearsexp to predict the salary for this model
# as it will be compared with the y_test

"""VISUALISING THE TRAINED SET


"""

plt.scatter(x_train , y_train , color = 'red')

plt.plot(x_train , lr.predict(x_train) , color = 'blue')

plt.title('salary vs yearsexperience (training set) ' )
plt.xlabel('Years of Experience')
plt.ylabel( ' Salary ')

plt.scatter(x_train , y_train , color = 'red')
plt.plot(x_train , lr.predict(x_train) , color = 'blue')
plt.title('salary vs yearsexperience (training set) ' )
plt.xlabel('Years of Experience')
plt.ylabel( ' Salary ')
plt.show()

"""VISUALISING THE TEST SET"""

"""x_train = Training data for Years of Experience.
lr.predict(x_train) = Model's predicted salaries for the training data"""

plt.scatter(x_test , y_test , color = 'red')
plt.plot(x_train , lr.predict(x_train) , color = 'blue') # regression line i.e predicted salary
plt.title('salary vs yearsexperience (testing set) ' )
plt.xlabel('Years of Experience')
plt.ylabel( ' Salary ')
plt.show()

"""FOR MAKING SINGLE PREDICTIONS"""

print(lr.predict([[12]]))
single = lr.predict( [[10.3]] )
print(single)
# predict method always except 2Darr as form of its i/p
#12→scalar [12]→1D array [[12]]→2D array

"""FINAL LINEAR EQUATION"""

print(lr.coef_)
print(lr.intercept_)

# y^ = b' + b1x1
# Where: y^ = Dependent variable (output) , b'(value of y when x=0) y-intercept
# and b1 is slope coeff(rate of change ofy with respect to x) x1 - independent variable(i/p)

salary = 25609.89799835482 + 9332.94473799 *YearsExperience


Use Linear Regression when data shows a straight-line trend.
Use Non-Linear Regression when data follows a curve and can't be well-represented by a straight line.
