from django.apps import AppConfig


class MovieSearcherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_searcher'
    
    # OMDB API configuration
    OMDB_API_KEY = 'c4caeeda'
    OMDB_API_URL = 'http://www.omdbapi.com/'
