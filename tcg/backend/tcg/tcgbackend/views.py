from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import MyModel
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = ItemSerializer