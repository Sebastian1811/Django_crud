from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from plato.models import Plato
from plato.models import Alimento

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = '__all__'