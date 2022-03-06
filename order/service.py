from icecream.models import IceCream
from order.models import Order, StatusChoices


class OrderService:
    def create(self, validated_data):

        icecreams = validated_data.pop("icecreams")

        order = Order.objects.create(**validated_data)
        icecreams = IceCream.objects.bulk_create(
            [
                IceCream(
                    order=order,
                    cone_wafer=icecream.get("cone_wafer"),
                    base_flavour=icecream.get("base_flavour"),
                    toppings=icecream.get("toppings"),
                )
                for icecream in icecreams
            ]
        )
        return order

    def update(self, order, validated_data):
        remarks = (
            validated_data.get("remarks")
            if validated_data.get("remarks")
            else order.remarks
        )
        order.remarks = remarks

        # if icecreams are set in request, previously set icecreams are wiped and the following ones are set
        if validated_data.get("icecreams"):
            icecreams = validated_data.get("icecreams")
            icecreams_to_be_created = IceCream.objects.bulk_create(
                [
                    IceCream(
                        cone_wafer=icecream.get("cone_wafer"),
                        base_flavour=icecream.get("base_flavour"),
                        toppings=icecream.get("toppings"),
                    )
                    for icecream in icecreams
                ]
            )
            order.icecreams.set(icecreams_to_be_created)
        order.save()
        return order

    def checkout(self, order, validated_data):
        order.address = validated_data.get("address")
        order.phone_number = validated_data.get("phone_number")
        order.status = StatusChoices.COMPLETED

        order.save()
        return order
