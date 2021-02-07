from django.db import models

# Create your models here.
class Challenge(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    url = models.CharField(max_length=300, default="")
    title = models.CharField(max_length=200, default="")
    

    def __str__(self):
        return self.title