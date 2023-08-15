from rest_framework import generics
from .models import Wiget
from .serializers import WigetSerializer
from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly

class WigetList(generics.ListAPIView):
    queryset = Wiget.objects.all()
    serializer_class = WigetSerializer

class WigetDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Wiget.objects.all()
    serializer_class = WigetSerializer
