Under Feature_Scaling 

Normalisation - scaling all values between 0 and 1

Under Normalisation comes the - 

1] MinMaxscaler - Use when Data is not Gaussian ,  scales values between 0 and 1,  Works well with Neural Networks 

Formula -  (x−min)/(max−min)

2] Mean Normalisation - makes the mean of the feature = 0 , the values are generally scaled between -1 and 1
Xnorm =  X−mean(X) / max(X)−min(X) 
​when you want zero-centered data , Useful when the data is not normally distributed


3] MaxAbs  - Scaling scales each feature by its maximum absolute value, so the values range from -1 to 1, but the mean is not centered at 0 unless the original data was centered 
Formual - Xscaled​ = X / ∣ Xmax |
Use when - For sparse data (e.g., when many values are zero) , When you don’t want to center data (i.e., keep zero entries as0)


4] RobustScaler -  scales the data using the median and the interquartile range (IQR = Q3 - Q1) instead of the mean and standard deviation.
It is robust to outliers, which means it reduces the effect of extreme values.
Formula - 𝑋scaled = 𝑋 − median / IQR

where -  Median is the center (middle) value of the data , IQR (Interquartile Range) is the difference between the 75th percentile (Q3) and 25th percentile (Q1).
Use - When your data contains many outliers , When mean and standard deviation are misleading

