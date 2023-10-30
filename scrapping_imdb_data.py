#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoupb


# In[18]:


import csv


# In[14]:


url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'


# In[15]:


response = requests.get(url)


# In[49]:


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    movies = soup.find_all('div', attrs = {'class':'lister-item mode-advanced'})
    
    with open('imdb_movies.csv', mode = 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Year', 'Rating', 'Genre'])
        
        for movie in movies:
            title = movie.h3.a.text
            
            year = movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(','').replace(')','')
            
            rating = movie.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n','')
            
            genre = movie.p.find('span', class_ ="genre").text.replace('\n','')
#             print (title, year, rating, genre)
            
            writer.writerow([title, year, rating, genre])
else:
    print('Failed to fetch data from IMDb.')

