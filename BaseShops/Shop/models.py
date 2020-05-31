from django.db import models
from streets.models import *


class Shop(models.Model):
    name = models.CharField(max_length=50)
    street = models.ForeignKey(Streets, on_delete=models.CASCADE)
    house = models.IntegerField()
    time_to_close = models.TimeField()
    time_to_open = models.TimeField()
