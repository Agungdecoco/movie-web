from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Movies

# Create your views here.

"""
View to list all movies.
"""
def movie_list(request):
    movies = Movies.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

"""
View to display detail from selected movie.
"""
def movie_detail(request, pk):
    if not str(pk).isdigit():
        return HttpResponseBadRequest("Invalid ID")
    movie = get_object_or_404(Movies, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
