from django.contrib import admin
from .models import Device, Calc

@admin.register(Device, Calc)
class MyAdmin(admin.ModelAdmin):
    pass
