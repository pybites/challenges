from django.contrib import admin
from .models import Device, Data

@admin.register(Device, Data)
class MyAdmin(admin.ModelAdmin):
    pass
