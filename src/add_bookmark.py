from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

def add_bookmark(movie_id):
    """Add this movie as a bookmark"""
   
    # update movies such that bookmark is set to true, which means it counts as a bookmark
    cur.execute("""
                UPDATE movies
                SET bookmark = true
                WHERE id = %s                
                """, 
                (movie_id,)
    )
    conn.commit()     

   
 

