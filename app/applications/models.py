from django.db import models
from django.conf import settings
from mixins.assets import TimeStampMixin
from clients.models import Client

from properties.models import Property

User = settings.AUTH_USER_MODEL


class Easement(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class LandUse(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ApplicationType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class IndividualApplication(TimeStampMixin):
    """
    An individual application for a land.
    """

    application_no = models.CharField(max_length=20, unique=True)
    file_no = models.CharField(max_length=20, unique=True)
    received = models.DateField("date received", null=True, blank=True)
    client = models.ManyToManyField(Client, blank=True)
    a_property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="property",)
    application_type = models.ManyToManyField(ApplicationType)
    land_use = models.ManyToManyField(LandUse)
    other_land_use = models.CharField(max_length=20, blank=True, null=True)
    easement = models.ManyToManyField(Easement)
    other_easement = models.CharField(max_length=20, blank=True, null=True)
