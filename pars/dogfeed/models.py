from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    name = models.TextField()

    def __str__(self):
        return self.name

class Amount(models.Model):
    name = models.ForeignKey(Pet,on_delete=models.CASCADE)
    weight = models.IntegerField()
    time = models.DateTimeField()
    
    