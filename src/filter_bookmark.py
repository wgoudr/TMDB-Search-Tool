from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

def filter_bookmark():
    """Fetch movies by bookmark"""
   
    # select all the movies that have a bookmark then Fetch all rows from the last executed query
    cur.execute("""SELECT * FROM movies WHERE bookmark = true """)
    movies = cur.fetchall()
    
    # Check if any movies were found, and print the title of the movie
    if movies:
        print(f"got them!")  
    else:
        print("No bookmarks were found")   

    return movies

