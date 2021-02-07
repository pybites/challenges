from django.urls import path
from users.views import UserUpdateView, UserPasswordChangeView, UserPasswordChangeDoneView

app_name = 'users'


urlpatterns = [
    path('<int:pk>', UserUpdateView.as_view(template_name='user.html'), name='user'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
]