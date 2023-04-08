from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from .serializers import TachesSerializer
from .models import Taches
from projets.models import Projets, Membres

# Create your views here.

@api_view(['GET'])
def findAll(request):
    taches=Taches.objects.all()
    serializer=TachesSerializer(taches,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPersonnel(request,id):
    data=request.data
    membres=Membres.objects.get(pk=id)
    taches=Taches.objects.create(membres=membres,projets=None, titre=data['titre'],deadline=data['deadline'], etat=data['etat'])
    print(data['titre'],data['deadline'], data['etat'], membres.pk)
    serializer=TachesSerializer(taches,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createGroupe(request,id_projets):
    data=request.data
    projets=Projets.objects.get(pk=id_projets)
    membres=Membres.objects.get(pk=data['id'])
    taches=Taches.objects.create(membres=membres,projets=projets, titre=data['titre'],deadline=data['deadline'], etat=data['etat'])
    print(data['titre'],data['deadline'], data['etat'], membres.pk)
    serializer=TachesSerializer(taches,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def findByProject(request,id):
     projets=Projets.objects.get(pk=id)
     taches=projets.taches_set.all()
     serializer=TachesSerializer(taches,many=True)
     return Response(serializer.data)

@api_view(['GET'])
def findOneByPk(request,id):
     membres=Membres.objects.get(pk=id)
     taches=membres.taches_set.all()
     serializer=TachesSerializer(taches,many=True)
     return Response(serializer.data)

@api_view(['PUT'])
def update(request,id):
     data=request.data
     taches=Taches.objects.get(pk=id)
     taches.etat=data['etat']
     taches.save()
     serializer=TachesSerializer(taches,many=False)
     return Response(serializer.data)