from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")

cur = conn.cursor()

def filter_by_genre(genre):
    """Fetch movies by genre."""
   
    # select all the movies with the genre id, also order them by rating in another query (not being used)
    cur.execute("""SELECT * FROM movies WHERE %s = ANY(genre_ids)""", (genre,))
    movies = cur.fetchall()   

    cur.execute("""SELECT * FROM movies WHERE %s = ANY(genre_ids) ORDER BY rating ASC""",(genre,))
    asc_movies = cur.fetchall()

    return movies, asc_movies

