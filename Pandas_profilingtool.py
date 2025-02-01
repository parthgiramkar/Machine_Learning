import pandas as pd

df = pd.read_csv('titanic.csv')

df.head()

"""This installs the ydata_profiling library, which is used for automatic data analysis and 
generating detailed reports & !is used to run this command in a Jupyter Notebook or similar environments"""
!pip install ydata_profiling

from ydata_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='output.html')
