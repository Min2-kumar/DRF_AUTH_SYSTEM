from django.urls import path
# from OTT_platform.api.view import movie_list, movie_details
from OTT_platform.api.view import (MovieListAPIView, MovieDetailsAPIView, UserReview, WatchListAPIView, 
                                    WatchListDetailAPIView, StreamPlatformAPIView,
                                    StreamPlatformDetailAPIView, ReviewList, ReviewDetail, ReviewCreate, UserReview)

urlpatterns = [
    # FBV
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-details'),

    # CBV - APIView
    path('list/', MovieListAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsAPIView.as_view(), name='movie-details'),

    # movies
    path('watchlist/', WatchListAPIView.as_view(), name='watchlist-list'),
    path('watchlist/<int:pk>/', WatchListDetailAPIView.as_view(), name='watchlist-detail'),

    # movie platform
    path('stream/', StreamPlatformAPIView.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='streamplatform-detail'),

    # review
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # filter by URL
    # path('reviews/<str:username>/', UserReview.as_view(), name='user-review-list'),
    path('reviews/', UserReview.as_view(), name='user-review-list'),

]
