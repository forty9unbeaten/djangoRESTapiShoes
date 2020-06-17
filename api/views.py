from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api import serializers
from shoes import models

# Create your views here.


class ShoeViewSet(ModelViewSet):
    serializer_class = serializers.ShoeSerializer
    queryset = models.Shoe.objects.all()


class ShoeTypeViewset(ModelViewSet):
    serializer_class = serializers.ShoeTypeSerializer
    queryset = models.ShoeType.objects.all()


class ShoeColorViewset(ModelViewSet):
    serializer_class = serializers.ShoeColorSerializer
    queryset = models.ShoeColor.objects.all()


class ManufacturerViewset(ModelViewSet):
    serializer_class = serializers.ManufacturerSerializer
    queryset = models.Manufacturer.objects.all()
