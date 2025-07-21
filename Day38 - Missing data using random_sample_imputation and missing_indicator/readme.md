Missing data for univariate imputation : -

For both numerical and categorical columns - using random_sample_imputation and missing_indicator
The missing indicator increase the overall accuracy of the model

Here , the distribution of data and variance are almost the same but we can see the diff in the co-variance of_data , -it changes.

Also ,it is memory_heavy_for_deployement , so can't be used_when the user is interacting, with the model as it will be taking extra space
