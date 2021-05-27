from rest_framework import serializers
from icecream.models import IceCream


class IceCreamModelSerializer(serializers.Serializer):
    cone_wafer = serializers.CharField()
    base_flavour = serializers.CharField()
    toppings = serializers.ListField()


class ConfigSerializer(serializers.Serializer):
    cone_wafers = serializers.ListField()
    base_flavours = serializers.ListField()
    toppings = serializers.ListField()