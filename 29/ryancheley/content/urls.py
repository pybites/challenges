from django.urls import path
from content.views import ContentTemplateView

app_name = 'content'


urlpatterns = [
    path('', ContentTemplateView.as_view(template_name='page.html'), name='home'),
    path('Pages/<str:name>', ContentTemplateView.as_view(template_name='page.html'), name='content'),
]