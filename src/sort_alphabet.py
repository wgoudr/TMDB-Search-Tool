from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

# sort alphabetically in descending order
def sort_alphabet(ordered):
    """Sort all movies in either ascending or descending alphabetical order"""
    
    # check variable passed on to do either ASC or DESC
    if ordered == "Ascending":
        cur.execute("""SELECT * FROM movies ORDER BY title ASC """)
        movies = cur.fetchall()

    if ordered == "Descending":
        cur.execute("""SELECT * FROM movies ORDER BY title DESC """)
        movies = cur.fetchall()
 
    return movies




