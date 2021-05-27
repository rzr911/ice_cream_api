from model_utils.models import TimeStampedModel, UUIDModel


class TimeStampedUUIDModel(TimeStampedModel, UUIDModel):
    class Meta(object):
        abstract = True
