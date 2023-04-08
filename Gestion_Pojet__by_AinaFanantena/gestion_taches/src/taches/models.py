from django.db import models

from projets.models import Projets, Membres

# Create your models here.

class Taches(models.Model):
    class Etat(models.IntegerChoices):
        en_cours=1,"En Cours"
        revue=2,"Revue"
        termine=3,"Terminé"
    membres=models.ForeignKey(Membres, on_delete=models.SET_NULL, default=models.SET_NULL, null=True)
    projets=models.ForeignKey(Projets, on_delete=models.SET_NULL, default=models.SET_NULL, null=True)
    titre=models.CharField(max_length=120)
    deadline=models.DateField(null=True)
    etat=models.PositiveSmallIntegerField(choices=Etat.choices, default=Etat.en_cours)
