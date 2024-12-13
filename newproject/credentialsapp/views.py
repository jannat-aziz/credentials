from django.shortcuts import render
from rest_framework import viewsets
from .models import Practitioner,Credential
from .serializers import PractitionerSerializer, CredentialsSerializer

# Create your views here.

class PractitionerViewSet(viewsets.ModelViewSet):

    queryset=Practitioner.objects.all()
    serializer_class= PractitionerSerializer

class CredentialsViewSet(viewsets.ModelViewSet):
 
    queryset= Credential.objects.all()
    serializer_class = CredentialsSerializer
    