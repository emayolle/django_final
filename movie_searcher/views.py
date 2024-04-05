from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Genre, Movie
from .forms import MovieForm

# Create your views here.


class IndexView(ListView):
    template_name = 'index.html'
    model = Movie
    paginate_by = 20
    context_object_name = 'movies'

    def get_queryset(self):
        title = self.request.GET.get('title')
        if title:
            return Movie.objects.prefetch_related('genres').filter(title__icontains=title)
        return Movie.objects.prefetch_related('genres').all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # print(self.request.GET.get('title'))

        ctx['movie_form'] = MovieForm(self.request.GET or None)

        return ctx