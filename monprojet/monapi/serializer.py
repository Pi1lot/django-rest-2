from rest_framework import serializers
from .models import Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["nom","prenom", "genre", "password", "email"]

# On fait un Serializer sans le champ "password" pour ne pas l'afficher
class ClientSerializerNoPass(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["nom", "prenom", "genre", "email"]
