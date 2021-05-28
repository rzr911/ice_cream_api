from rest_framework import serializers
from icecream.models import IceCream


class IceCreamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = ("cone_wafer", "base_flavour", "toppings")
