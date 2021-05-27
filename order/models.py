from django.utils.translation import gettext_lazy as _
from django.db import models
from base.models import TimeStampedUUIDModel


class StatusChoices(models.TextChoices):
    CREATED = "created", _("Created")
    COMPLETED = "completed", _("Completed")


class Order(TimeStampedUUIDModel):
    remarks = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        default=StatusChoices.CREATED,
        choices=StatusChoices.choices,
        null=False,
        blank=False,
    )
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
