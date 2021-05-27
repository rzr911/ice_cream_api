from rest_framework import serializers

from icecream.serializers import IceCreamModelSerializer
from order.models import StatusChoices


class OrderCreateUpdateReadSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    icecreams = IceCreamModelSerializer(many=True)
    remarks = serializers.CharField()
    address = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)


class OrderCheckoutSerializer(serializers.Serializer):
    address = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
