import requests
from .models import Movie

from django.conf import settings

TMDB_TOKEN = settings.TMDB_TOKEN


def fetch_and_save_movies():
    genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    genre_response = requests.get(genre_url, headers=headers)
    genre_data = genre_response.json()
    genre_map = {g["id"]: g["name"] for g in genre_data["genres"]}

    for page in range(1,32):
         movie_url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&page={page}"
         movie_response = requests.get(movie_url, headers=headers)
         movie_data = movie_response.json()
   

 
    for item in movie_data["results"]:
        genres = [genre_map[g] for g in item.get("genre_ids", [])]

        Movie.objects.get_or_create(
            tmdb_id=item["id"],
            defaults={
                "title": item["title"],
                "description": item.get("overview", ""),
                "poster_url": item.get("backdrop_path"),
                "genre": ", ".join(genres),
            }
        )

    print("Movies saved successfully")
