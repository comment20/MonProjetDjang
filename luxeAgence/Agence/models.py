from django.db import models
class utilisateur(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    date_joined=models.DateTimeField(auto_now_add=True)
    
#  creation d'une nouvelle class
class Note(models.Model):
    francais = models.FloatField()
    histoire_geo = models.FloatField()
    anglais = models.FloatField()
    mathematiques = models.FloatField()
    physique_chimie = models.FloatField()


    


# Create your models here.
