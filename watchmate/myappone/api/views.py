from rest_framework.response import Response
from rest_framework.decorators import api_view
from myappone.models import Movie
from myappone.api.serializers import MovieSerializer


# ---------------------------------------------------------------------------------------------------------------------
# by default: set for 'GET' request
# 'many=True' is used because of extracting more than one object

@api_view()                                                 
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)         
    return Response(serializer.data)


# ---------------------------------------------------------------------------------------------------------------------
# by default: set for 'GET' request

@api_view()                                                 
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
