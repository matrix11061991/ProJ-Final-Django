from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Membres
class MembreSerializer(serializers.ModelSerializer):
    class Meta:
       model = Membres
       fields = '__all__'
