from django.shortcuts import render
from myappone.models import Movie
from django.http import HttpResponse, JsonResponse

# Create your views here.


# --------------------------------------------------------------------------------------------
# def movie_list(request):
#     movies = Movie.objects.all()
#     print(list(movies.values()))
#     return HttpResponse(list(movies.values()))


# --------------------------------------------------------------------------------------------
def movie_list(request):
    movies = Movie.objects.all()
    
    data = {
        'movies':list(movies.values())
    }

    return JsonResponse(data)
