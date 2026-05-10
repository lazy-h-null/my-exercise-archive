from django.db import models
from django.utils import timezone

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    born_in_captivity = models.BooleanField(default=False)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']