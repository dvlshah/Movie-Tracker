from rest_framework.generics import ListAPIView
from movies.models import Movies

class PostListAPIView(ListAPIView):
    queryset = Movies.objects.all()

    
