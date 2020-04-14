from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from users.forms import CustomUserCreationForm
from django_registration.backends.activation.views import RegistrationView

urlpatterns = [
    path('stadium/', include('stadium_tracker.urls')),
    path('backend/', admin.site.urls),
    path('users/', include('users.urls')),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=CustomUserCreationForm), name='django_registration_register'),
    path(r'accounts/', include('django_registration.backends.activation.urls')),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'api/', include('api.urls')),
    path('', include('content.urls')),

]
