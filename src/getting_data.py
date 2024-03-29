from flask import Flask, render_template
import requests
import psycopg2
import time
import os
from dotenv import load_dotenv
load_dotenv()

# i want to see how long this takes, not important
start_time = time.time()


#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

# url for the request for genre. Movies has a {page} variable to loop over multiple pages and is declared later
url_genres = "https://api.themoviedb.org/3/genre/movie/list?language=en"

#every request needs a header for authorization
# find bearer key from env
api_key = os.getenv('API_KEY')
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# send the request and receive response and convert to json for genre
response_genres = requests.get(url_genres, headers=headers)
data_genres = response_genres.json()

#parse through reponse for genres request and add to database
for genre in data_genres['genres']:
    cur.execute("""INSERT INTO genres (id, name) VALUES (%s, %s)
                ON CONFLICT (id) DO NOTHING; """,
                (genre['id'], genre['name'])
                )        

#send request for a set amount of pages for the movies table and insert them to the table 
page = 1
for x in range(1,10):
    page = x
    url_movies = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page}&sort_by=popularity.desc"
    response_movies = requests.get(url_movies, headers=headers)
    data_movies = response_movies.json()
    
    for movie in data_movies['results']:
        
        # checking for errors, if theres no release_date, set release date to none
        release_date = movie.get('release_date', None) or None

        # add everything from the request into the movie table
        cur.execute("""INSERT INTO movies (id, title, genre_ids, release_date, rating) VALUES (%s, %s, %s, %s, %s)                
                    ON CONFLICT (id) DO NOTHING;""",
                    (movie['id'], movie['title'], movie['genre_ids'], release_date, movie['vote_average'])
                    )
    
#commit and close the connection and cursor after doing everything
conn.commit()
conn.close()
cur.close()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")





