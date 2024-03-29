from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

def delete_bookmark(movie_id):
    """Delte a bookmark for a movie"""
   
    # Update the movies table to set bookmark to fale, which makes it not a bookmark anymore
    cur.execute("""
                UPDATE movies
                SET bookmark = false
                WHERE id = %s                
                """, 
                (movie_id,)
    )
    conn.commit()      
  
   
 