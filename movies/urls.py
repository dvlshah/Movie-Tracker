import django.conf.urls
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    django.conf.urls.url(r'^$', views.movies, name='movie_list'),
    django.conf.urls.url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    #django.conf.urls.url(r'^movies/', views.MovieList.as_view()),
]
