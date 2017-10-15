import django.shortcuts
from django.http import HttpResponse
from django.http import Http404
from .models import Movies,Actor,Director
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tables import MoviesTable

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

#def movies(request):
	#table = Movies(Movies.objects.all())
	#table.paginate(page=request.GET.get('page', 1), per_page=10)
#	return django.shortcuts.render(request, 'movies/movie_list.html', {'movies':Movies.objects.all()})
    #return django.shortcuts.render(request, 'movies/movie_list.html', {'movies': Movies.objects.all()})

def movies(request):
	table = MoviesTable(Movies.objects.all())
	table.paginate(page=request.GET.get('page', 1), per_page=10)
	return django.shortcuts.render(request, 'movies/movie_list.html', {'table': table})
