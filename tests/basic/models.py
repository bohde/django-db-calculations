from django.db import models
from db_calculations.managers import CalculationManager

class Number(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    objects = CalculationManager()
