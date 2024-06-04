from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializer import ClientSerializer, ClientSerializerNoPass
import random
import json
class ClientListApiView(APIView):
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializerNoPass(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'nom': request.data.get('nom'),
            'prenom': request.data.get('prenom'),
            'genre': request.data.get('genre'),
            'password': request.data.get('password'),
            'email': request.data.get('email'),
        }
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailApiView(APIView):
    def post(self, request, id, *args, **kwargs):
        client = Client.objects.get(pk=id)  # (ou id=id qui fonctionne aussi)
        if not Client:
            return Response({"res": "Object with id does not exists"},
                            status=status.HTTP_400_BAD_REQUEST
                            )

        # Récupérer le contenu de du POST et le re-transformer en JSON/ Dictionnaire
        # Pour comparer les valeur dans la database vs celles envoyés.
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # print(body)

        content = body['password']

        # print(body['password'])
        # print(client.password)
        if client.password == content:
            authenticated = True
        else:
            authenticated = False

        data = {
                "is_auth": authenticated,
            }

        # On retourne True si les deux passwords matchent.
        return Response(data, status=status.HTTP_200_OK)

    def get(self, request, id, *args, **kwargs):
        client = Client.objects.get(pk=id)  # (ou id=id qui fonctionne aussi)
        if not Client:
            return Response({"res": "Object with id does not exists"},
                            status=status.HTTP_400_BAD_REQUEST
                            )

        serializer = ClientSerializerNoPass(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        client = Client.object.get(pk=id)  # (ou id=id qui fonctionne aussi)

        if not client:
            return Response(
                {"res": "Object␣with␣id␣does␣not␣exists"},
                status=status.HTTP_400_BAD_REQUEST)
        client.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)


    def put(self, request, id, *args, **kwargs):
        client = Client.object.get(pk=id)  # (ou id=id qui fonctionne aussi)
        if not client:
            return Response(
                {"res": "Object␣with␣id␣does␣not␣exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'titre': request.data.get('titre'),
            'commentaire': request.data.get('commentaire'),
        }
        serializer = ClientSerializer(instance=client, data=data, partial=
            True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
