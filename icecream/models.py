from django.db import models
from django.contrib.postgres.fields import ArrayField
from base.models import TimeStampedUUIDModel


cone_flavours = [("plain", "Plain"), ("chocolate", "Chocolate"), ("waffle", "Waffle")]
base_flavours = [("vanilla", "Vanilla"), ("chocolate", "Chocolate"), ("mango", "Mango"), ("strawberry","Strawberry"), ("coconut","Coconut")]
toppings = [("Tutti Frutti", "Tutti Frutti"), ("Chocolate Chips", "Chocolate Chips"), ("Roasted Almonds", "Roasted Almonds")]

class IceCream(TimeStampedUUIDModel):
    cone_wafer = models.CharField(max_length=150, choices=cone_flavours, null=False
    )

    base_flavour = models.CharField(max_length=150, choices=base_flavours, null=False)

    toppings = ArrayField(models.CharField(max_length=150, choices=toppings, blank=False))

    order = models.ForeignKey(
        "order.Order", null=True, related_name="icecreams", on_delete=models.CASCADE
    )