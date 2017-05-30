from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=50)
    consumption = models.FloatField()

class Data(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    time = models.FloatField()
    cost = models.FloatField()
