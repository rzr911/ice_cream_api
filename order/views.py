from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from order.models import Order, StatusChoices
from order.serializers import OrderCreateUpdateReadSerializer, OrderCheckoutSerializer
from order.service import OrderService


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related("icecreams")
    service = OrderService()

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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        order = self.service.create(serializer.validated_data)
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        data = request.data
        order = self.get_object()
        serializer = self.get_serializer(data=data, instance=order, partial=partial)
        serializer.is_valid(raise_exception=True)

        order = self.service.update(
            order=order, validated_data=serializer.validated_data
        )
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def checkout(self, request, *args, **kwargs):
        data = request.data
        order = self.get_object()

        # Order that is Completed should not be allowed to be modified
        if order.status == StatusChoices.COMPLETED:
            return Response(
                data="Completed Order cannot be checked out again",
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=data, instance=order, partial=False)
        serializer.is_valid(raise_exception=True)

        order = self.service.checkout(
            order=order, validated_data=serializer.validated_data
        )

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
