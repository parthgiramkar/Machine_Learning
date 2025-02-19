#necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# here header = none means that the that the dataset has no name to first row
#and then we define it
df = pd.read_csv('wine_data.csv' , header = None , usecols = [ 0, 1 , 2 ] )
df.columns = [ 'CLASS LABEL' , 'ALCOHOL' , 'MALIC ACID' ]
df

sns.kdeplot(df['ALCOHOL'])
# here density is the  probabibity density

sns.kdeplot(df['MALIC ACID'])

color_dict = {3:'red',1:'green',2:'blue'}
#hue	- Decides which column will be used to assign colors.
#palette - 	Defines what colors are used for different hue values.
#here class label(col) is plotted as colors
sns.scatterplot(x=df['ALCOHOL'], y=df['MALIC ACID'] , hue = df['CLASS LABEL'] , palette = color_dict)

"""NOW THE TRAIN TEST SPLIT"""

from sklearn.model_selection import train_test_split
#dropped the last col for x and stored itin  y , what to drop axis = 1(i.e col) for class label
x_test , x_train , y_test , y_train = train_test_split( df.drop('CLASS LABEL' , axis = 1) , df['CLASS LABEL'] , test_size = 0.3 , random_state = 0 )
y_train.shape , x_train.shape , x_test.shape

# NORMALISATION STARTS
from sklearn.preprocessing import MinMaxScaler
sc  =  MinMaxScaler()
#fit to calc the xmin and xmax
sc.fit(x_train)
#apply the transformation to both train&test of x
x_train_scaled = sc.transform(x_train)
x_test_scaled = sc.transform(x_test)

x_train_scaled

# so to change the array format  as given by the sklearn convert it to readable format
# using the pandas dataframe(caps) and also give name to cols
x_train_scaled = pd.DataFrame(x_train_scaled , columns = x_train.columns)
x_test_scaled = pd.DataFrame(x_test_scaled , columns = x_test.columns)

x_test_scaled

#the first value overall stastics
np.round(x_test.describe() , 1)

#compare the both old new one to normalised method
#and see the min and max which is of imp(0,1)
np.round(x_train_scaled.describe() , 1)

#THEN COMES THE EFFECT OF SCALING
fig , (ax1 , ax2 ) = plt.subplots( ncols = 2 , figsize = (12,5) )

ax1.scatter(x_train['ALCOHOL'] , x_train['MALIC ACID'] )
ax1.set_title('before scaling')

ax2.scatter(x_train['ALCOHOL'] , x_train['MALIC ACID'] )
ax2.set_title('after scaling')

plt.show()

fig , (ax1 , ax2 ) = plt.subplots( ncols = 2 , figsize = (12,5) )
# In Matplotlib's scatter() function, the c parameter is used to set colors for each data
# point based on a given array.
ax1.scatter(x_train['ALCOHOL'] , x_train['MALIC ACID'] , c = y_train)
ax1.set_title('before scaling')
#y_train means the class label(col)
ax2.scatter(x_train_scaled['ALCOHOL'] , x_train_scaled['MALIC ACID'] , c = y_train )
ax2.set_title('after scaling')
# you can't seee there's much  difference  in shape

#now using the seaborn library
figure , (axes1 , axes2) = plt.subplots(ncols = 2 , figsize = ( 12  ,5 ) )
axes1.set_title = "before scaling"

sns.kdeplot( x_train['ALCOHOL'] , ax = axes1  )
sns.kdeplot( x_train['MALIC ACID'] , ax = axes1 )

sns.kdeplot( x_train_scaled['ALCOHOL'] , ax = axes2  )
sns.kdeplot( x_train_scaled['MALIC ACID'] , ax = axes2 )
#now both are on the same scale

"""NOW INDIVIDUALLY TESTING THE SCALING EFFECTS"""

figure , (axes1 , axes2) = plt.subplots(ncols = 2 , figsize = ( 12  , 5 ) )
axes1.set_title = "before alcohol scaling"
sns.kdeplot( x_train['ALCOHOL'] , ax = axes1  )

axes1.set_title = "after  alcohol scaling"
sns.kdeplot( x_train_scaled['ALCOHOL'] , ax = axes2  )
#no change apart from the scale

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# before scaling
ax1.set_title('Malic acid Distribution Before Scaling')
sns.kdeplot(x_train['MALIC ACID'], ax=ax1)

# after scaling
ax2.set_title('Malic acid Distribution After Standard Scaling')
sns.kdeplot(x_train_scaled['MALIC ACID'], ax=ax2)
plt.show()
