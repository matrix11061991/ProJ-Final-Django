from django.db import models

# Create your models here.

class Membres(models.Model):
    username=models.CharField(max_length=120, unique=True)
    email=models.EmailField()
    mot_de_passe=models.CharField(max_length=10)
    avatar=models.ImageField(upload_to="products/", blank=True, null=True)
