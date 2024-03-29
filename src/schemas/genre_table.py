from flask import Flask, render_template
import requests
import psycopg2

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")

cur = conn.cursor()

#make a genre table
cur.execute(""" 
            CREATE TABLE IF NOT EXISTS genres (
            id INT PRIMARY KEY,
            name VARCHAR(255)           
);
""")

conn.commit()
conn.close()
cur.close()