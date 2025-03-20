import pandas as pd    #HTTP (HyperText Transfer Protocol) is a protocol used for communication between web browsers and web servers.
import requests           #to make HTTP requests to fetch data from APIs.

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMzZiMjAxOWU3NWFmZGVlZWNmZjgzZGM0MTNjYmIxMyIsIm5iZiI6MTczNzQ2NTI1My4zNDIwMDAyLCJzdWIiOiI2NzhmOWRhNTAxYTcxYWNhNTRmMDhhYTgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Vph5mrhxnX7Es_Y3Lx63vos4kdbcPbLdD93gB9MqCkI"
}

response = requests.get(url, headers=headers)           #sends an HTTP GET request to the TMDb API for authentication.

print(response.json())

url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"          #fetch the top rated movies from the page1

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMzZiMjAxOWU3NWFmZGVlZWNmZjgzZGM0MTNjYmIxMyIsIm5iZiI6MTczNzQ2NTI1My4zNDIwMDAyLCJzdWIiOiI2NzhmOWRhNTAxYTcxYWNhNTRmMDhhYTgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Vph5mrhxnX7Es_Y3Lx63vos4kdbcPbLdD93gB9MqCkI"
}

response = requests.get(url, headers=headers)

response.json()          #as its dictionary we convert it to list into which they are list in which present are  dictionaries

response.json()['results']       #so now in complete json format of desired , so extracting the result key which contains the deatil

# in TMDb API response, the "results" key contains a list of dictionaries where in each contains movie with details like id, title, vote_average etc

pd.DataFrame(response.json()['results'])         #in a good readable manner

#selecting the required columns i.e 9 , so total movies - 10043*9(dimn)   in 2d array form as we to put in table not series of
pd.DataFrame(response.json()['results'])[['id','original_language','original_title','overview','popularity','release_date','title','vote_average','vote_count']]

temp_df = pd.DataFrame(response.json()['results'])[['id','original_language','original_title','overview','popularity','release_date','title','vote_average','vote_count']]

temp_df.head()   #starting five i.e the top five

df = pd.DataFrame()             #put the empty

df

for i in range(1,503) :                                  #running the loop for all pages
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={}".format(i)       #Dynamically updates the url by inserting the page number using .format(i)

    headers = {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMzZiMjAxOWU3NWFmZGVlZWNmZjgzZGM0MTNjYmIxMyIsIm5iZiI6MTczNzQ2NTI1My4zNDIwMDAyLCJzdWIiOiI2NzhmOWRhNTAxYTcxYWNhNTRmMDhhYTgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Vph5mrhxnX7Es_Y3Lx63vos4kdbcPbLdD93gB9MqCkI"
    }

    response = requests.get(url, headers=headers)

import pandas as pd
import requests

df = pd.DataFrame()

for i in range(1, 503):
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={}".format(i)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMzZiMjAxOWU3NWFmZGVlZWNmZjgzZGM0MTNjYmIxMyIsIm5iZiI6MTczNzQ2NTI1My4zNDIwMDAyLCJzdWIiOiI2NzhmOWRhNTAxYTcxYWNhNTRmMDhhYTgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Vph5mrhxnX7Es_Y3Lx63vos4kdbcPbLdD93gB9MqCkI"
    }

    response = requests.get(url, headers=headers)

    # Check if the response is successful(http code=200) and contains the 'results' key
    if response.status_code == 200 and 'results' in response.json():
        temp_df = pd.DataFrame(response.json()['results'])[['id', 'original_language', 'original_title', 'overview', 'popularity', 'release_date', 'title', 'vote_average', 'vote_count']]
        df = pd.concat([df, temp_df], ignore_index=True)                # after the loop the index should be 20 not 1-19 return

df

df.shape

df.to_csv("movies_data.csv", index=False)
#Saves the df DataFrame into a CSV file named "movies_data.csv"
#index=False ensures that the row index is not included in the CSV file

from google.colab import files
files.download("movies_data.csv")

