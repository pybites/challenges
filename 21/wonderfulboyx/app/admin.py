from django.contrib import admin
from .models import Device, Person

@admin.register(Device, Person)
class MyAdmin(admin.ModelAdmin):
    pass
