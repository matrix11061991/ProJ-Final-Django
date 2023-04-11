from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    motdepasse = models.CharField(max_length=100)
