from django.urls import path

from . import views

from .views import (
    TweetListView,
    FilteredTweetListView
)


urlpatterns = [
    path('', TweetListView.as_view(), name='tweets-home'),
    path('tweets', TweetListView.as_view(), name='tweets-home'),
    path('tweets/<str:hashtag>', FilteredTweetListView.as_view(), name='tweets-filtered'),
    path('about/', views.about, name='tweets-about'),
]