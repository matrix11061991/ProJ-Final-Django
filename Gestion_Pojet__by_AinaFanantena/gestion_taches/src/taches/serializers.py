from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Taches
class TachesSerializer(serializers.ModelSerializer):
    class Meta:
       model = Taches
       fields = '__all__'
