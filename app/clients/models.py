import uuid

from django.db import models
from locations.models import District
from mixins.assets import TimeStampMixin
from django.utils.text import slugify
from django.urls import reverse


class Title(TimeStampMixin):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Occupation(TimeStampMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Client(TimeStampMixin):
    title = models.ForeignKey("Title", on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    middle_name = models.CharField(max_length=254, blank=True, null=True)
    slug = models.SlugField(max_length=254, blank=True, unique=True)
    occupation = models.ForeignKey(
        "Occupation", on_delete=models.CASCADE, blank=True, null=True
    )
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    address1 = models.CharField(max_length=254, blank=True, null=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("clients:client-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("clients:client-update", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.last_name[:3]
                + self.first_name[:3]
                + " - "
                + str(uuid.uuid4().hex[:6])
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.last_name + ", " + self.first_name
