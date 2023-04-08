from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from .serializers import MembreSerializer
from .models import Membres

# Create your views here.

@api_view(['GET'])
def findAll(request):
    membres=Membres.objects.all()
    serializer=MembreSerializer(membres,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    data=request.data
    membres=Membres.objects.create(username=data['username'], email=data['email'], mot_de_passe=data['mot_de_passe'], avatar=data['avatar'])
    #print(data['username'],data['email'], data['mot_de_passe'], =data['avatar'])
    serializer=MembreSerializer(membres,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def findOne(request):
    data=request.data
    print(data["email"])
    membres=Membres.objects.filter(email=data['email'], mot_de_passe=data["mot_de_passe"])
    serializer=MembreSerializer(membres,many=True)
    if len(serializer.data)>0:
        return Response(serializer.data)
    else:
        return Response("not found")

@api_view(['PUT'])
def update(request, id):
    data=request.data
    membres=Membres.objects.get(pk=id)
    membres.email=data["email"]
    membres.mot_de_passe=data["mot_de_passe"]
    membres.username=data["username"]
    membres.save()
    serializer=MembreSerializer(membres,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def findOneByPk(request,id):
     membres=Membres.objects.get(pk=id)
     serializer=MembreSerializer(membres,many=False)
     return Response(serializer.data)
