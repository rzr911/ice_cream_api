from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.postgres.fields import ArrayField
from base.models import TimeStampedUUIDModel


class ConeFlavourChoices(models.TextChoices):
    PLAIN = "plain", _("Plain")
    CHOCOLATE = "chocolate", _("Chocolate")
    WAFFLE = "waffle", ("Waffle")


class BaseFlavourChoices(models.TextChoices):
    VANILLA = "vanilla", _("Vanilla")
    CHOCOLATE = "chocolate", _("Chocolate")
    MANGO = "mango", _("Mango")
    STRAWBERRY = "strawberry", _("Strawberry")
    COCONUT = "coconut", _("Coconut")


class ToppingChoices(models.TextChoices):

    TUTTI_FRUTTI = "Tutti Frutti", _("Tutti Frutti")
    CHOCOLATE_CHIP = "Chocolate Chips", _("Chocolate Chips")
    ROASTED_ALMOND = "Roasted Almonds", _("Roasted Almonds")


class IceCream(TimeStampedUUIDModel):
    cone_wafer = models.CharField(
        max_length=150, choices=ConeFlavourChoices.choices, null=False
    )

    base_flavour = models.CharField(
        max_length=150, choices=BaseFlavourChoices.choices, null=False
    )

    toppings = ArrayField(
        models.CharField(max_length=150, choices=ToppingChoices.choices, blank=False)
    )

    order = models.ForeignKey(
        "order.Order", null=True, related_name="icecreams", on_delete=models.CASCADE
    )
