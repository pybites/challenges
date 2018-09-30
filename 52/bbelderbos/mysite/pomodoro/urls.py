from django.urls import path

from . import views

app_name = 'pomodoro'
urlpatterns = [
    path('', views.track_pomodoro, name='track_pomodoro'),
]
