"""Importing the library"""



import numpy as np
import matplotlib.pyplot as py     #.pyplot to access the pyplot module from matplotlib
import pandas as pd



"""Importing the dataset"""

#pandas lib function is used
dataset = pd.read_csv('Data.csv')

#for independent variable i.e input
x = dataset.iloc[ : , : -1].values                           #iloc function of pandas lib(locate index) lbound:upperb -the range of row and cols respectively the ub gets excluded
                                                            #.values this converts the DataFrame into a NumPy array
#for dependent variable i.e output
y = dataset.iloc[ : , -1].values

print(x)

print(y)

"""Replacing the Missing Data"""

#By taking the average of that column
from sklearn.impute import SimpleImputer           #SimpleImputer class from sklearn.impute is a part of the scikit-learn library used to handle missing data in datasets
imputer = SimpleImputer( missing_values=np.nan , strategy='mean' )         #creating object of that class , means to find the nan value of that col
imputer.fit(x[ : , 1:3])                             #Fit It only computes the required statistics no changes are made to the dataset..
x[ : , 1:3] = imputer.transform(x[ : , 1:3])             #transform method is used to replace the missing values and reassinged to x[ : , 1:3] impute means missing data

print(x)

"""Encoding Categorical Data i.e country col(ind)"""

#Use One-Hot Encoding when the categorical feature has no natural ordering features like "Color" (Red, Blue, Green) or "Animal" (Dog, Cat, Bird) are nominal
# Not Too Many Unique Categories
from sklearn.compose import ColumnTransformer         #ColumnTransformer in scikit-learn is used to apply transformations to specific columns of your dataset ,while allowing other cols to remain unchanged
from sklearn.preprocessing import OneHotEncoder       #combined with OneHotEncoder, it can efficiently handle categorical data by encoding categorical cols into binary vectors

ct =  ColumnTransformer( transformers =[ ( 'encoder' , OneHotEncoder() , [0 ]) ] , remainder='passthrough' )  #as onehtenc is class i.e which method to apply remainder='passthrough' i.e salary&age where onehtenc will not be applied                                             #creating obj of class three arg - 1.    2.type of encoding 3.on index we want to apply onehtenc
x = np.array(ct.fit_transform(x))         #as used above but now in combine form
# particularly useful when your dataset has both categorical and numerical features the lib
#  synatx : - ColumnTransformer(transformers=[(name, transformer, columns)], remainder='passthrough')  the transfomers is a tuple

print(x)

"""  Encoding the Dependent variables(purchased col)"""

from sklearn.preprocessing import LabelEncoder                    #LabelEncoder A class used to convert categorical labels into numerical labels.
le = LabelEncoder()
y = le.fit_transform(y)                              #OneHotEncoder: The class that defines how to convert categorical data into binary vectors.fit_transform: The method that applies the encoding process by:
                                              #Learning the unique categories (fit) Transforming the data into one-hot-encoded vectors (transform).

print(y)

"""Splitting the dataset into training set and testing set"""

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split( x ,y , test_size=0.2 , random_state=1)  #test_size=0.2 means it will predict 2 cases 8 will be for training
#with random_state=1, the output will be the same every time, giving you the same training and testing data.
#If you do not set random_state (i.e., leave it as the default, which is None), the random shuffling will be different every time the code is executed.
#train_test_split function returns two pairs of arrays: one for x and for y dataset change in order then mismatch

print(x_train)

print( x_test )

print( y_train )                                #these 8 y_train coressponds to the 8 same x_train

print(y_test)

#Feature Scaling After Train-Test Split Prevents Data Leakage Ensures Unbiased Testing:

"""Feature Scaling ----  . It involves transforming the features (input variables) in a dataset so that they are on the same scale, 
making the model training more efficient and stable. common method - Standardization (also known as Z-score normalization) is 
widely used in many ml algorithms  especially when features have different scales or units."""

from sklearn.preprocessing import StandardScaler     #StandardScaler is used for feature scaling i.e standardization, which transforms the data to
sc = StandardScaler()                                                    #have a mean of 0 and a standard deviation of 1.sc = StandardScaler()

x_train[:, :3] = sc.fit_transform(x_train[:, :3])
x_test[:, 3:] = sc.transform(x_test[:, 3:])     #fit_transformto intger variable only not the dummy var
 #transform() method applies the scaling learned from x_train to x_test

print(x_train)

print(x_test)


"""
 1 ] pandas : - 
Role: Handling and analyzing data.
Key Points:
Works with tabular data (like Excel sheets) using DataFrames.
Helps in reading data from files (CSV, Excel), cleaning, and manipulating it.
Example: pd.read_csv('data.csv') reads data from a CSV file.

2 ] matplotlib.pyplot (as plt):
Role: Creating visualizations.
Key Points:
Used to make graphs like line plots, bar charts, histograms, etc.
Helps in visualizing data trends and patterns.
Example: plt.plot(x, y) creates a line plot.

3] numpy (as np):
Role: Working with numerical data.
Key Points:
Handles arrays (like lists but faster and more powerful).
Supports mathematical operations (like addition, multiplication) on large datasets.
Example: np.array([1, 2, 3]) creates a NumPy array.
"""
