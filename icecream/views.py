from django.shortcuts import render
from rest_framework import viewsets

from icecream.models import ConeWafer, BaseFlavour, Topping
from icecream.serializers import (
    ConeWaferModelSerializer,
    BaseFlavourModelSerializer,
    ToppingModelSerializer,
)


class ConeWaferViewSet(viewsets.ModelViewSet):
    queryset = ConeWafer.objects.all()
    serializer_class = ConeWaferModelSerializer


class BaseFlavourViewSet(viewsets.ModelViewSet):
    queryset = BaseFlavour.objects.all()
    serializer_class = BaseFlavourModelSerializer


class ToppingFlavourViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingModelSerializer
