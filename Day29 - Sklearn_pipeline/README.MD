With Pipeline  - used to chain multiple steps (transformers + model) together in ml workflow

pipe = Pipeline( [ ('trf1' , tf1) , ('trf2' , tf2) , ('trf3' , tf3) , ('trf4' , tf4) , ('trf5' , tf5) ] )

Each step is a tuple -
The first value is the name you assign to that step (string).
The second value is the transformer or estimator object

Also , increasing the overall accuracy as compared to_the  other one_code
