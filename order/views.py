from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status, viewsets
from rest_framework.response import Response

from icecream.models import IceCream
from order.models import Order, StatusChoices
from order.serializers import OrderCreateUpdateReadSerializer, OrderCheckoutSerializer
from rest_framework.decorators import action


class OrderViewset(viewsets.ModelViewSet):
    queryset = (
        Order.objects.all()
        .prefetch_related("icecreams")
    )

    def get_serializer_class(self):
        serializers = {
            "list": OrderCreateUpdateReadSerializer,
            "create": OrderCreateUpdateReadSerializer,
            "retrieve": OrderCreateUpdateReadSerializer,
            "update": OrderCreateUpdateReadSerializer,
            "partial_update": OrderCreateUpdateReadSerializer,
            "checkout": OrderCheckoutSerializer,
        }
        return serializers.get(self.action)
    permission_classes = []

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        icecreams = serializer.validated_data.pop("icecreams")

        order = Order.objects.create(**serializer.validated_data)
        icecreams = IceCream.objects.bulk_create([IceCream(order=order, cone_wafer=icecream.get(
            "cone_wafer"), base_flavour=icecream.get("base_flavour"), toppings=icecream.get("toppings")) for icecream in icecreams])

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        data = request.data
        order = self.get_object()
        serializer = self.get_serializer(
            data=data, instance=order, partial=partial
        )
        serializer.is_valid(raise_exception=True)

        remarks = data.get("remarks") if data.get("remarks") else order.remarks
        order.remarks = remarks

        if data.get("icecreams"):
            icecreams = data.get("icecreams")
            icecreams_to_be_created = IceCream.objects.bulk_create([IceCream(cone_wafer=icecream.get(
                "cone_wafer"), base_flavour=icecream.get("base_flavour"), toppings=icecream.get("toppings")) for icecream in icecreams])
            order.icecreams.set(icecreams_to_be_created)
        order.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def checkout(self, request, *args, **kwargs):
        data = request.data
        order = self.get_object()

        serializer = self.get_serializer(
            data=data, instance=order, partial=False
        )
        serializer.is_valid(raise_exception=True)

        if order.status == StatusChoices.COMPLETED:
            return Response(message="", status=status.HTTP_400_BAD_REQUEST)

        order.address = serializer.validated_data.get("address")
        order.phone_number = serializer.validated_data.get("phone_number")
        order.status = StatusChoices.COMPLETED

        order.save()

        serializer = self.get_serializer(order)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )
