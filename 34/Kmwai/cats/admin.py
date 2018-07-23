from django.contrib import admin
from .models import Cats


@admin.register(Cats)
class CatAdmin(admin.ModelAdmin):
    fields = ('name', 'genus', 'species', 'binomial_name')

