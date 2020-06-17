from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Amount(models.Model):
    name = models.ForeignKey(Pet,on_delete=models.CASCADE)
    weight = models.IntegerField()
    time = models.DateTimeField()
    
    