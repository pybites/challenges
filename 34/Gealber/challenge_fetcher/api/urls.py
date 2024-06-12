from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('challenges/', views.ChallengeList.as_view()),
    path('challenges/<int:pk>/', views.ChallengeDetail.as_view()),
]

