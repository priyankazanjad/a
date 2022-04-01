from django.db import models

# Create your models here.
class Person(models.Model):
    id=models.IntegerField()
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

