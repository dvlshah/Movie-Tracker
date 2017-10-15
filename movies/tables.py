import django_tables2 as tables
from .models import Movies

class MoviesTable(tables.Table):
    class Meta:
        model = Movies
        attrs = { 'class': 'paleblue' }
