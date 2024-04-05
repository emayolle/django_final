from movie_searcher.models import Genre, Movie
from faker import Faker

fake = Faker()

for _ in range(10):
    Genre.objects.create(name=fake.word())

for _ in range(100):
    movie = Movie.objects.create(title=fake.sentence(), year=fake.year())
    movie.genres.set(Genre.objects.order_by('?')[:3])
    movie.save()