from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

# end and start dates from last month (assuming that is february and db is static)
end_date = "2024-02-29"
start_date = "2024-02-01"

def best_movies_feb():
    """Sort all movies by date for the last month"""
   
    # select all the movies in February and sort them by rating
    cur.execute("""SELECT release_date, title, rating, id
                FROM movies 
                WHERE release_date 
                BETWEEN %s AND %s 
                ORDER BY rating DESC""", 
                (start_date, end_date))
    
    movies = cur.fetchall()

    return movies   

