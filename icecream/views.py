from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream.models import IceCream, cone_flavours, base_flavours, toppings
from icecream.serializers import ConfigSerializer
from rest_framework.decorators import action


class ConfigView(APIView):

    def get(self, request, *args, **kwargs):
        cone_flavours = cone_flavours
        base_flavours = base_flavours
        toppings = toppings

        serializer = ConfigSerializer(cone_flavours=cone_flavours, base_flavours=base_flavours, toppings=toppings)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )
