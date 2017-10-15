import django.shortcuts
from django.http import HttpResponse
from django.http import Http404
from .models import Movies,Actor,Director
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
	html = ""
	all_movies = Movies.objects.all()
	#template = loader.get_template('movies/index.html')
	context = {
		'all_movies':all_movies,
	}
	return django.shortcuts.render(request, 'movies/index.html', context)

def detail(request,movie_id):
	try:
		movie = Movies.objects.get(pk=int(movie_id))
	except Movies.DoesNotExist:
		raise Http404("Movie with the given ID does not exist")
	return django.shortcuts.render(request, 'movies/detail.html', {'movies':movie})

def movies(request):
    return django.shortcuts.render(request, 'movies/movie_list.html', {'movies': Movies.objects.all()})
