import requests
from flask import Flask

app = Flask(__name__)

def get_movies(how_many,list_type):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

# def get_movie_info(movie):
#     return Movie(movie['id'], movie['original_title'], movie['poster_path'])


# @app.context_processor
# def utility_processor():
#     def tmdb_image_url(path, size):
#         return tmdb_client.get_poster_url(path, size)
#     return {"tmdb_image_url": tmdb_image_url}

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMWZkOGI2NjdiYzQyNTg5OWQzMWYyMDA0NTNkMGEyYSIsInN1YiI6IjYzZjNhMjc4MTUzNzZjMDA4MzM3Mzc3NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iZs5vlLy9Qm-GQ-DyG573_6DOegGeOv_GeWWg2yQRSU"



def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()