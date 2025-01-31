import pandas as pd

df = pd.read_csv('titanic.csv')

print(df)

df.head()               # the top 5rows means it gives you the preview of the data

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(df ['Survived'] )

