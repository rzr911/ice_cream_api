from django.db import models
from base.models import TimeStampedUUIDModel


class ConeWafer(TimeStampedUUIDModel):
    name = models.CharField(max_length=150, unique=True, null=False)


class BaseFlavour(TimeStampedUUIDModel):
    name = models.CharField(max_length=150, unique=True, null=False)


class Topping(TimeStampedUUIDModel):
    name = models.CharField(max_length=150, unique=True, null=False)
