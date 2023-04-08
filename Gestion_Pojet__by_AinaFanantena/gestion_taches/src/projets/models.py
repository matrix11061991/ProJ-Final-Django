from django.db import models
from membres.models import Membres

# Create your models here.

class Projets(models.Model):
    class Etat(models.IntegerChoices):
        en_cours=1,"En Cours"
        revue=2,"Revue"
        termine=3,"Terminé"
    admins=models.ForeignKey(Membres, on_delete=models.CASCADE)
    nom_projet=models.CharField(max_length=150, blank=False)
    debut=models.DateField(blank=True)
    deadline=models.DateField(blank=False)
    etat_projet=models.PositiveSmallIntegerField(choices=Etat.choices, default=Etat.en_cours)
