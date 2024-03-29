from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

# sort rating in descending order
def sort_by_rating(ordered):
    """Sort all movies by rating in either descending or ascending order"""

    # select all the movies and sort them by rating in ASC or DESC
    if ordered == "Ascending":
        cur.execute(f"""SELECT * FROM movies ORDER BY rating ASC """)
        movies = cur.fetchall()

    if ordered == "Descending":
        cur.execute(f"""SELECT * FROM movies ORDER BY rating DESC """)
        movies = cur.fetchall()

    
    return movies