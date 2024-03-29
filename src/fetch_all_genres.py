from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

def fetch_all_genres():
    """Fetch the table for all the genres"""
   
    # select all the genres
    cur.execute("""SELECT * FROM genres""")
    genres = cur.fetchall()   

    return genres
