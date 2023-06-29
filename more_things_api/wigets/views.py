from rest_framework import generics
from .models import Wiget
from .serializers import WigetSerializer
from django.shortcuts import render

class WigetList(generics.ListAPIView):
    queryset = Wiget.objects.all()
    serializer_class = WigetSerializer

class WigetDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wiget.objects.all()
    serializer_class = WigetSerializer