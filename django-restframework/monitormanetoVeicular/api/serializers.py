from rest_framework import serializers
from .models import dadosVeicular

class dadosVeicularSerializer(serializers.ModelSerializer):

    class Meta:
        model = dadosVeicular
        fields= '__all__'