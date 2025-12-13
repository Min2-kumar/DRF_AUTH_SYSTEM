from rest_framework.response import Response
from rest_framework.decorators import api_view

from OTT_platform.models import Movie
from OTT_platform.api.serializers import MovieSerializer

@api_view()     # this gives only 'GET'
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)