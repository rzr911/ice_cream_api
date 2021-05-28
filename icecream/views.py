from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream.models import ConeFlavourChoices, BaseFlavourChoices, ToppingChoices


class ConfigView(APIView):
    def get(self, request, *args, **kwargs):
        cone_flavours = ConeFlavourChoices.values
        base_flavours = BaseFlavourChoices.values
        toppings = ToppingChoices.values

        return Response(
            data={
                "cone_flavours": cone_flavours,
                "base_flavours": base_flavours,
                "toppings": toppings,
            },
            status=status.HTTP_200_OK,
        )
