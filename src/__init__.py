from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from .filter_bookmark import filter_bookmark
from .filter_by_genre import filter_by_genre
from .best_movies_feb import best_movies_feb
from .sort_by_release import sort_by_release
from .fetch_all_genres import fetch_all_genres
from .sort_alphabet import sort_alphabet
from .add_bookmark import add_bookmark
from .sort_by_rating import sort_by_rating
from .delete_bookmark import delete_bookmark

#connect to postgres database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1917", port="5432")
cur = conn.cursor()

# where application is run
def create_app(test_config=None):

    # instance of application
    app = Flask(__name__, instance_relative_config=True)    

    # for text configuration
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY="dev",
        )    
    else:
        app.config.from_mapping(test_config)

    # check for any errors and send them to error page
    @app.errorhandler(Exception)
    def handle_error(error):
        error_message = str(error)
        return render_template("error_page.html", error_message=error_message)


    # routes GET requests
    @app.get("/")
    def Index():
        movies = best_movies_feb()
        return render_template('index.html', movies=movies)
    
    # Find Movies by Their Release Date
    @app.get("/movie_by_release")
    def movies_by_release():
        return render_template("movies_by_release.html")
    
    @app.get("/movie_by_release/<ordered>")
    def ascending_release(ordered):
        movies = sort_by_release(ordered)
        return render_template("movies_by_release.html", movies=movies)

    # Find Movies by Genre
    @app.get("/movies_by_genre")
    def fetch_genre():
        genres = fetch_all_genres()
        return render_template("movies_by_genre.html", genres=genres)
        
    @app.get("/movies_by_genre/<genre>")
    def movie_by_genre(genre):
        movies = filter_by_genre(genre)[0]        
        genres = fetch_all_genres()
        return render_template("movies_by_genre.html", movies=movies, genres=genres)    
    
    # Here are The Best Movies From The Last Month
    @app.get("/movies_last_month")
    def movies_last_month():
        movies = best_movies_feb()
        return render_template("best_movies_feb.html", movies=movies) 

    # Find Bookmarks   
    @app.get("/bookmarks")
    def bookmark():
        movies = filter_bookmark()
        return render_template("bookmarks.html", movies=movies) 
    # Find Movies Alphabetically
    @app.get("/movies_alphabetical")
    def movies_alphabetical():
        return render_template("movies_alphabetical.html")
    
    @app.get("/movies_alphabetical/<ordered>")
    def movies_alphabetical_ordered(ordered):
        movies = sort_alphabet(ordered)
        return render_template("movies_alphabetical.html", movies=movies)
    
    # Find Movies by Rating
    @app.get("/movies_by_rating")
    def movies_rated():        
        return render_template("movies_by_rating.html")
    
    @app.get("/movies_by_rating/<ordered>")
    def movies_rated_ordered(ordered):
        movies = sort_by_rating(ordered)
        return render_template("movies_by_rating.html", movies=movies)    
    

    # routes POST requests which are all bookmark requests
    @app.post("/bookmark/delete")
    def delete_a_bookmark():
        movie = request.form["movie_id"]
        delete_bookmark(movie)
        movies = filter_bookmark()
        return render_template("bookmarks.html", movies=movies)
 
    @app.post("/bookmark/best_movies_feb")
    def add_to_bookmark_bestfeb():
        movie = request.form["movie_id"]
        add_bookmark(movie)
        movies = best_movies_feb()
        return render_template("best_movies_feb.html", movies=movies)    

    @app.post("/bookmark/alphabetical")
    def add_to_bookmark():
        movie = request.form["movie_id"]
        add_bookmark(movie)
        return render_template("movies_alphabetical.html")

    @app.post("/bookmark/genre")
    def add_to_bookmark_genre():
        movie = request.form["movie_id"]
        add_bookmark(movie)
        genres = fetch_all_genres()
        return render_template("movies_by_genre.html",genres=genres )
    
    @app.post("/bookmark/rating")
    def add_to_bookmark_rating():
        movie = request.form["movie_id"]
        add_bookmark(movie)
        genres = fetch_all_genres()
        return render_template("movies_by_rating.html")
    
    @app.post("/bookmark/release")
    def add_to_bookmark_release():
        movie = request.form["movie_id"]
        add_bookmark(movie)
        genres = fetch_all_genres()
        return render_template("movies_by_release.html")
    
    
    return app

