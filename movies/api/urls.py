from django.conf.urls import url
from django.contrib import admin

from .views import (
    MoviesDeleteAPIView,
    MoviesListAPIView,
    MoviesRetrieveAPIView,
    MoviesUpdateAPIView
)

urlpatterns = [
    url(r'^$',MoviesListAPIView.as_view(),name='list'),
    url(r'^(?P<name>[\w-]+)/$',MoviesRetrieveAPIView.as_view(),name='retrieve'),
    url(r'^(?P<name>[\w-]+)/edit/$',MoviesUpdateAPIView.as_view(),name='update'),
    url(r'^(?P<name>[\w-]+)/delete/$',MoviesDeleteAPIView.as_view(),name='delete'),
]
