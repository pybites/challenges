from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.apps, name='apps'),
    url(r'^show$', views.show, name='show'),
    url(r'^create_company$', views.create_company, name='create_company'),
    url(r'^create_device$', views.create_device, name='create_device'),
]
