from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class Cats(models.Model):
    """cat model"""
    name = models.CharField(max_length=255)
    genus = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    binomial_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' belongs to the ' + self.genus + ' genus.'

    def __repr__(self):
        return self.name + ' was added.'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

