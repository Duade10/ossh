from django.db import models
from core.models import AbstractTimestampModel


class Member(AbstractTimestampModel):
    image = models.ImageField(upload_to="team/member", blank=True, null=True)
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
