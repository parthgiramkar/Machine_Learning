Overfitting happens when a machine learning model : - 


Performs very well on training data but fails to generalize to new, unseen data.
in other words , the model memorizes the data instead of learning patterns.

To avoid overfitting, always :-
Split your dataset into: Training set (for learning) and  Validation/test set (for checking performance)

The train_test_split() method is used to split our data into train and test sets. First, we need to divide our data into features (X) and labels (y). The dataframe gets divided into X_train, X_test, y_train, and y_test. X_train and y_train sets are used for training and fitting the model. The X_test and y_test sets are used for testing the model if it's predicting the right outputs/labels. It is suggested to keep our train sets larger than the test sets.

after train_test_split - In machine learning value of features may have different ranges and units. This variation can impact negatively on the performance of algorithms like KNN, SVM or Logistic Regression. To avoid this issue feature scaling is used to standardize data - 

Feature scaling makes sure that all features (columns) in your dataset are on the same scale, which is important for many algorithms.
Here ,we have used StandardScaler() - also known as Z-score normalization.
It standardizes features by removing the mean and scaling to unit variance:
                            z =(x -μ)/σ            
   
Where:x = original value
μ = mean of the feature
σ = standard deviation of the feature
After StandardScaler, the transformed data has - Mean = 0 , Standard deviation = 1
 So values typically fall between -3 and +3 , DO feature scaling after train_test_split to prevent data leakage

fit() — Learn from the data
Calculates the statistics needed for transformation.

scaler.fit(X_train)  # Learns parameters like mean, std
  transform() — Apply what it learned
Actually scales the data using what it learned during fit().

X_train_scaled = scaler.transform(X_train)  # Uses learned mean and std to scale

Only used on training data on ,  test_data use only the transform() not fit it will apply values of training_set to testing_set by doing this 
IF we apply FIT_TRANSFORM ON TEST THEN THE MODEL WILL be OVERFITTING



