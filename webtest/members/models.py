from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)



# Create your models here.

class Manager(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('NAME', max_length=64)
    date = models.DateField('DATE')
    time = models.TimeField('TIME')
    #image = models.ImageField('PICTURE')

