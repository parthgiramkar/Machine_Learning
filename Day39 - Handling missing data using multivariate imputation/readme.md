KNNImputer calculates distances (Euclidean distance) between rows .
Disadv - 
At production time, cannot_be used as it performs calculations at prediction time as it is stored also in the training_set , it cannot be trained before hand , thus taking verytime to load . So , its best for training/Offline pre-processing

 Euclidean dist = 
      Distance = sqrt{w_1 (x_1 - x_1')^2 + w_2 (x_2 - x_2')^2  + w_n (x_n - x_n')^2}
where w=total_coordinates/present co-ordinates

