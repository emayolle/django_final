import requests
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Genre, Movie
from .forms import MovieForm
from .apps import MovieSearcherConfig

class IndexView(ListView):
    """
    View for displaying a list of movies based on search criteria.

    Attributes:
        template_name (str): The name of the template to be rendered.
        model (Model): The model class to be used for retrieving movie data.
        paginate_by (int): The number of movies to display per page.
        context_object_name (str): The name of the context variable containing the movie list.

    Methods:
        get_queryset(): Retrieves the movie list based on search criteria.
        get_context_data(**kwargs): Adds additional context data to be passed to the template.
    """
    template_name = 'index.html'
    model = Movie
    paginate_by = 20
    context_object_name = 'movies'

    def get_queryset(self):
        """
        Retrieves the movie list based on search criteria.

        Returns:
            QuerySet: The queryset containing the filtered movies.
        """
        title = self.request.GET.get('title')
        if title:
            movies = Movie.objects.prefetch_related('genres').filter(title__icontains=title)

            # Create a list of existing movie titles to avoid duplicates
            existing_movies = movies.values_list('title', flat=True)

            # Search for movies using the OMDB API
            movies_result = requests.get(f"{MovieSearcherConfig.OMDB_API_URL}?apikey={MovieSearcherConfig.OMDB_API_KEY}&s={title}")
            
            # Check if the API request was successful
            if movies_result.status_code == 200:
                movies_data = movies_result.json()

                # Check if the API response contains movie data
                if movies_data['Response'] == 'True' and movies_data['totalResults'] != '0':

                    # Loop through the search results and create Movie objects
                    for movie in movies_data['Search']:                

                        # Check if the movie title already exists in the database            
                        if movie.get('Title') not in existing_movies:

                            # Retrieve detailed information about the movie
                            movie_detail_result = requests.get(f"{MovieSearcherConfig.OMDB_API_URL}?apikey={MovieSearcherConfig.OMDB_API_KEY}&i={movie.get('imdbID')}")
                            movie_detail = movie_detail_result.json()

                            # Check if the API request was successful
                            if movie_detail_result.status_code == 200 and movie_detail['Response'] == 'True':

                                # Create Genre objects and associate them with the Movie object
                                genres = []
                                for genre in movie_detail['Genre'].split(','):
                                    genre_obj, created = Genre.objects.get_or_create(name=genre.strip())
                                    genres.append(genre_obj)

                                # Create the Movie object
                                movie_obj = Movie.objects.create(
                                    title=movie.get('Title'),
                                    year=movie.get('Year'),
                                )
                                movie_obj.genres.set(genres)
                                movie_obj.save()

                    # Update the movie list with the newly added movies
                    movies = Movie.objects.prefetch_related('genres').filter(title__icontains=title)   
   
            return movies
        return Movie.objects.prefetch_related('genres').all()

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to be passed to the template.

        Returns:
            dict: The context data.
        """
        ctx = super().get_context_data(**kwargs)

        ctx['movie_form'] = MovieForm(self.request.GET or None)

        return ctx