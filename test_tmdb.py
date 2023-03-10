import unittest
import pytest

import tmdb_client
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
   # Підготовка даних
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Виклик коду, який ми тестуємо
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Порівняння результатів
   assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

   # def get_movies_list(list_type):
   #  endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
   #  headers = {
   #      "Authorization": f"Bearer {API_TOKEN}"
   #  }
   #  response = requests.get(endpoint, headers=headers)
   #  response.raise_for_status()
   #  return response.json()

def test_get_movies_list(monkeypatch):
   # Список, який поверне прихований "запит до API".
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Результат запиту до API
   response = requests_mock.return_value
   # Ми перевизначаємо результат виклику методу json().
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

# def get_single_movie(movie_id):
#     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

def test_get_single_movie(monkeypatch):
    mock_single_movie = " "
    single_movie_mock = Mock()
    single_movie_mock.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.get_single_movie", single_movie_mock)
    single_movie = tmdb_client.get_single_movie
    assert single_movie == mock_single_movie


def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = " "
    cast_single_movie_mock = Mock()
    cast_single_movie_mock.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.get_single_movie", cast_single_movie_mock)
    single_movie_cast = tmdb_client.get_single_movie(550)
    assert single_movie_cast == mock_single_movie_cast


def test_get_movie_images(monkeypatch):
    mock_movie_images = " .jpg"
    movie_images_mock = Mock()
    movie_images_mock.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.get_movie_images", movie_images_mock)
    movie_images = tmdb_client.get_movie_images(550)
    assert movie_images == mock_movie_images