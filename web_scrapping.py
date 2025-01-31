
import pandas as pd
import requests
from bs4 import BeautifulSoup                     #used for scrapping web

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) hrome/80.0.3987.162 Safari/537.36'}
webpage = requests.get('https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav' , headers=headers).text

soup =  BeautifulSoup( webpage , 'lxml')
print( soup.prettify() )

company = soup.find_all('div' , class_='companyCardWrapper')

len(soup.find_all('div' , class_='companyCardWrapper') )

name = []
rating = []
reviews = []

for i in company :
    name.append(i.find('h2').text.strip() )
    rating.append(i.find('div' , class_='rating_text').text.strip())
    reviews.append(i.find('span' , class_='companyCardWrapper__ActionCount').text.strip() )



name

rating

reviews

"""# New Section"""

soup.find_all('h1')[0].text.strip()

# Get all <h2> elements, extract their text, and strip leading/trailing spaces
h2_texts = [h2.text.strip() for h2 in soup.find_all('h2')]

# Join the list with a newline for each element
result = '\n'.join(h2_texts)

# Print the result
print(result)

len(soup.find_all('h2'))

for i in soup.find_all('h2'):
    print(i.text.strip())               #strip for removing the spaces

for i in soup.find_all('p'):
  print(i.text.strip())

soup.find_all('p' , class_ ='rating' )

for i in soup.find_all('a'):
  print(i.text.strip())

soup.find_all('a' , class_ ='companyCardWrapper_' )
