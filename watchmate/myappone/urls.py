from django.urls import path
from myappone.views import movie_list

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
]
