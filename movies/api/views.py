from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from movies.models import Movies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieListSerializer,MovieRetrieveSerializer

"""
class MovieList(APIView):
	#Return all the movies
	def get(self,request):
		movies = Movies.objects.all()
		serializer = movieSerializer(movies,many=True)
		return Response(serializer.data)
"""

class MoviesListAPIView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieListSerializer

class MoviesRetrieveAPIView(RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieRetrieveSerializer
    lookup_field = 'name'
    #lookup_url_kwarg = "abc"

class MoviesUpdateAPIView(UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieRetrieveSerializer
    lookup_field = 'name'

class MoviesDeleteAPIView(DestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieRetrieveSerializer
    lookup_field = 'name'
