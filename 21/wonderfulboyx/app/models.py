from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=50)
    consumption = models.FloatField()

    def __str__(self):
        return self.name + "(" + str(self.consumption) +  "W)"

class Campany(models.Model):
    name = models.CharField(max_length=50)
    charge = models.FloatField()

    def __str__(self):
        return self.name + "(" + str(self.charge) + "/kWh)"

class Calc(models.Model):
    campany = models.ForeignKey(Campany,on_delete=models.CASCADE)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    time = models.FloatField()

    @property
    def cost(self):
        print('HELLOS')
        cost = str(float(self.campany.charge)*float(self.device.consumption)*float(self.time))
        return cost

    def __str__(self):
        return self.cost
