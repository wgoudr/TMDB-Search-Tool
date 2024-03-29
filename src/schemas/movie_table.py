from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")

cur = conn.cursor()

#making a movie table
cur.execute(""" 
            CREATE TABLE IF NOT EXISTS movies (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            genre_ids INT[],
            release_date DATE,
            rating NUMERIC(4, 2),
            bookmark BOOLEAN DEFAULT FALSE
);
""")

conn.commit()
conn.close()
cur.close()