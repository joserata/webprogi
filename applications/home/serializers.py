from rest_framework import serializers
from .models import Definiciones, Documentos, Normatividad, Eventos

class DefinicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definiciones
        fields = '__all__'

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = '__all__'

class NormatividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Normatividad
        fields = '__all__'

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'
