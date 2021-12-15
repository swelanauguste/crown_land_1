import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from locations.models import District
from mixins.assets import TimeStampMixin


def property_images_directory_path(instance, filename):
    return "client_id_images/{0}/{1}".format(instance.id_number, filename)


class Property(TimeStampMixin):
    """
    Property model
    """

    block = models.CharField(max_length=5)
    parcel = models.CharField(max_length=3)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    survey_plan_number = models.CharField(max_length=100, blank=True)

    location = models.CharField(max_length=255)
    quarter = models.ForeignKey(
        District,
        related_name="property_districts",
        on_delete=models.SET_NULL,
        null=True,
    )
    is_queens_chain = models.BooleanField("is queen's chain", default=False)
    # i_occupy = models.BooleanField(
    #     "Are you presently in occupation of this property?", default=False
    # )
    # year_occupied = models.IntegerField(blank=True, default=0)
    lot_size = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, default=0, help_text="in sq. ft."
    )
    details = models.TextField(blank=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ["block", "parcel"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.block + " - " + self.parcel + " - " + str(uuid.uuid4().hex[:6])
            )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("properties:property-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("properties:property-update", kwargs={"slug": self.slug})

    def __str__(self):
        return self.block + "-" + self.parcel
