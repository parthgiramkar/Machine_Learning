import pandas as pd

df = pd.read_csv('titanic.csv')

df.head()

!pip install ydata_profiling

from ydata_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='output.html')
