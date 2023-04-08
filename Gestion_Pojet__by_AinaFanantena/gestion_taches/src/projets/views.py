from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from .serializers import ProjetsSerializer
from .models import Projets, Membres

# Create your views here.

#Afficher toutes les listes projets
@api_view(['GET'])
def findAll(request):
    projets=Projets.objects.all()
    serializer=ProjetsSerializer(projets,many=True)
    return Response(serializer.data)

#Création d'une projet
@api_view(['POST'])
def create(request,fk):
    data=request.data
    membres=Membres.objects.get(pk=fk)
    projets=Projets.objects.create(admins=membres, nom_projet=data["nom_projet"], debut=data['debut'], deadline=data['deadline'], etat_projet=data['etat_projet'])
    print(fk, data["nom_projet"], data['debut'], data['deadline'], data['etat_projet'])
    serializer=ProjetsSerializer(projets,many=False)
    return Response(serializer.data)

#Afficher toutes les listes projets où l'utilisateur une tache
@api_view(['GET'])
def findOneByPk(request, id):
    membres=Membres.objects.get(pk=id)
    projets=membres.projets_set.all()
    serializer=ProjetsSerializer(projets,many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request,id):
     data=request.data
     projets=Projets.objects.get(pk=id)
     projets.etat_projet=data['etat']
     projets.save()
     serializer=ProjetsSerializer(projets,many=False)
     return Response(serializer.data)