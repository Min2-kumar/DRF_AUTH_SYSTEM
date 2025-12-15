from django.urls import path
# from OTT_platform.api.view import movie_list, movie_details
from OTT_platform.api.view import MovieListAPIView, MovieDetailsAPIView

urlpatterns = [
    # FBV
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-details'),

    # CBV - APIView
    path('list/', MovieListAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsAPIView.as_view(), name='movie-details'),
]
