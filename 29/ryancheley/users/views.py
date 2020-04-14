from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import CustomUser
from users.forms import CustomUserChangeForm
from django.urls import reverse, reverse_lazy


# Create your views here.

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    # fields = ['email', 'username', 'twitter_user', 'instagram_user', 'favorite_team']
    form_class = CustomUserChangeForm
    template_name = 'user.html'

    def get_success_url(self):
        return reverse('users:user', kwargs={
            'pk': self.object.pk,
        })

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id


class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'password_change_form.html'


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'
