from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/cats/(?P<pk>[0-9]+)$', views.get_delete_update_cat, name='get_delete_update_cat'),
    url(r'^api/v1/cats/$', views.get_post_cats, name='get_post_cats')
]