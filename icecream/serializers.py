from rest_framework import serializers
from icecream.models import ConeWafer, BaseFlavour, Topping


class ConeWaferModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConeWafer
        fields = "__all__"


class BaseFlavourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseFlavour
        fields = "__all__"


class ToppingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"
