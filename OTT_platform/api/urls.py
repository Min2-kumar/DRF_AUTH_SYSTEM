from django.urls import path
# from OTT_platform.api.view import movie_list, movie_details
from OTT_platform.api.view import MovieListAPIView, MovieDetailsAPIView, WatchListAPIView, WatchListDetailAPIView, StreamPlatformAPIView, StreamPlatformDetailAPIView

urlpatterns = [
    # FBV
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-details'),

    # CBV - APIView
    path('list/', MovieListAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsAPIView.as_view(), name='movie-details'),

    # movies
    path('watchlist/', WatchListAPIView.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', WatchListDetailAPIView.as_view(), name='watch-details'),

    # movie platform
    path('platform/', StreamPlatformAPIView.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='platform-details'),
]
