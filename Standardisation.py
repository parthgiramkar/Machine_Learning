import pandas as pd   #for data preprocessing
import seaborn as sns
import numpy as np            #for linear algebra
import matplotlib.pyplot as plt

df = pd.read_csv('Social_Network_Ads.csv')

df = df.iloc[ : , 2: ]          #works on numerical data

df.head()  #starting 5

df.sample(7)       #any random

"""RECOMMENDED to do train-test-split"""

from sklearn.model_selection import train_test_split
#this time used seperately x and y as eariler                                                      #30% test set
x_train , x_test , y_train , y_test = train_test_split(df.drop('Purchased' , axis =1), df['Purchased'] ,test_size = 0.3 , random_state = 0)

# for x -drop('Purchased', axis=1) means:'Purchased': The column to remove(drop) , axis=1: Refers to columns(to be droped not rows).
# for y -['Purchased']: Selects only this column as a Series (1D array) so in o/p
# do not print col print only row as its only one series(1d array) .

print( x_train.shape , x_test.shape )
print( y_train.shape , y_test.shape ) # returns

"""       StandardScaler : -"""

from sklearn.preprocessing import StandardScaler  #transforms the data so that it has s.d of 1 and mean =0
sc = StandardScaler()

#fit method to calc mean and s.d
sc.fit(x_train)        #learns the parameters of x_train and apply transformation to both x_train&test

x_train_scaled = sc.transform(x_train)    #tranformation to trained data means applying formula
x_test_scaled  = sc.transform(x_test)
#When you use sc.transform(x_train), it converts the scaled values into a NumPy array because
# StandardScaler is part of scikit-learn, which works primarily with arrays for efficient computations.

sc.mean_       #mean of the both x column

x_train

x_test_scaled

x_train_scaled

# so have to conv the array into pandas df for tabular format
#When you apply StandardScaler, the output (x_train_scaled) is a NumPy array,
#which does not have column names—just raw values.
#To make the data readable and structured like the original Pandas DataFrame, we
#reassign the original column names.


x_train_scaled = pd.DataFrame(x_train_scaled, columns=x_train.columns)
x_test_scaled = pd.DataFrame(x_test_scaled, columns=x_test.columns)
x_train_scaled

#calculates statistical metrics for all numerical columns in x_train.
x_train.describe()

#p.round(data, 1) rounds all values in x_train.describe() to one decimal place.
np.round(x_train_scaled.describe(), 1)

"""EFFECT OF *SCALING*


"""

figure  , ( axes1 , axes2 ) = plt.subplots( ncols = 2 , figsize = (12 , 5 ) )
#unit is inches, so (12, 5) means 12 inches wide and 5 inches tall.
"""Creates a single figure (fig) with two columns (ncols=2)
ax1 → Left plot (Before Scaling).
ax2 → Right plot (After Scaling)."""

axes1.scatter(x_train['Age'] , x_train['EstimatedSalary'] )
axes1.set_title('before scaling')

axes2.scatter(x_train_scaled['Age'] , x_train_scaled['EstimatedSalary'] , color = 'red' )
axes2.set_title('after scaling')

plt.show()

figure  , ( axes1 , axes2 ) = plt.subplots( ncols = 2 , figsize = (12 , 5 ) )
#unit is inches, so (12, 5) means 12 inches wide and 5 inches tall.
"""Creates a single figure (fig) with two columns (ncols=2)
ax1 → Left plot (Before Scaling).
ax2 → Right plot (After Scaling)."""
axes1.scatter(x_train['Age'] , x_train['EstimatedSalary'] )
axes1.set_title('BEFORE scaling')
axes2.scatter(x_train_scaled['Age'] , x_train_scaled['EstimatedSalary'] , color = 'red' )
axes2.set_title('AFTER scaling')

figure , (axes1 , axes2 ) = plt.subplots( ncols =2 , figsize = (12 ,5 ) )
""" sns.kdeplot(...) is used to plot a Kernel Density Estimation (KDE) curve.
KDE plots show the distribution of data, similar to histograms but smoother.
ax=ax1 means we plot these distributions in the first subplot (ax1). """

#before scaling
axes1.set_title('Before Scaling')
sns.kdeplot(x_train['Age'], ax = axes1)
sns.kdeplot(x_train['EstimatedSalary'], ax = axes1 )
plt.show()

# after scaling
axes2.set_title('After Standard Scaling')
sns.kdeplot(x_train_scaled['Age'], ax=axes2)
sns.kdeplot(x_train_scaled['EstimatedSalary'], ax=axes2)
plt.show()

figure , (axes1 , axes2 ) = plt.subplots( ncols =2 , figsize = (12 ,5 ) )
axes1.set_title('Before Scaling')
sns.kdeplot(x_train['Age'], ax = axes1)
sns.kdeplot(x_train['EstimatedSalary'], ax = axes1 )
axes2.set_title('After Standard Scaling')
sns.kdeplot(x_train_scaled['Age'], ax=axes2)
sns.kdeplot(x_train_scaled['EstimatedSalary'], ax=axes2



//Pandas DataFrame stores data in tabular form,  while .values extracts onlythe raw numerical values as a NumPy array.
//Efficient Computations – NumPy operations are faster and consume less memory compared to Pandas operations. 
//Required by Some ML Libraries – Many machine learning libraries (like Scikit-Learn) expect input in the form of a NumPy array instead of a Pandas DataFrame.
