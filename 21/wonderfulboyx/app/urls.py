from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.apps, name='apps'),
    url(r'^name$', views.apps, name='apps'),
]
