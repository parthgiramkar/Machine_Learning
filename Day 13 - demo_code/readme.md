Overfitting happens when a machine learning model : - 


Performs very well on training data but fails to generalize to new, unseen data.
in other words , the model memorizes the data instead of learning patterns.

To avoid overfitting, always :-
Split your dataset into: Training set (for learning) and  Validation/test set (for checking performance)

The train_test_split() method is used to split our data into train and test sets. First, we need to divide our data into features (X) and labels (y). The dataframe gets divided into X_train, X_test, y_train, and y_test. X_train and y_train sets are used for training and fitting the model. The X_test and y_test sets are used for testing the model if it's predicting the right outputs/labels. It is suggested to keep our train sets larger than the test sets.
