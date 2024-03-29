from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()


def sort_by_release(ordered):
    """Sort all movies by release date in either descending or ascending order"""
    
    # select all the movies and sort them by release date in ASC or DESC
    if ordered == "Ascending":
        cur.execute("""SELECT * FROM movies ORDER BY release_date ASC """)
        movies = cur.fetchall()

    if ordered == "Descending":
        cur.execute("""SELECT * FROM movies ORDER BY release_date DESC """)
        movies = cur.fetchall() 
    
    return movies



