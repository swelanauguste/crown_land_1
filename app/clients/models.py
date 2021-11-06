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


# class Occupation(TimeStampMixin):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title


class Client(TimeStampMixin):
    title = models.ForeignKey("Title", on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    middle_name = models.CharField(max_length=254, blank=True, null=True)
    slug = models.SlugField(max_length=254, blank=True, unique=True)
    occupation = models.CharField(max_length=254, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField("Primary tel", max_length=20, null=True)
    phone1 = models.CharField("Mobile tel", max_length=20, blank=True, null=True)
    phone2 = models.CharField("Home tel", max_length=20, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    address1 = models.CharField(max_length=254, blank=True, null=True)
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, blank=True, null=True
    )
    nationality = models.CharField(max_length=254, blank=True, null=True)

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


def client_id_image_directory_path(instance, filename):
    return "client_id_images/{0}/{1}".format(instance.id_number, filename)


class ClientIdentification(TimeStampMixin):
    identification = models.ForeignKey(
        Client,
        related_name="client_identifications",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    FORM_OF_ID = (
        ("National ID", "National ID"),
        ("Passport", "Passport"),
        ("Driving License", "Driving License"),
    )
    form_of_id = models.CharField(max_length=100, choices=FORM_OF_ID)
    id_number = models.CharField(max_length=100, unique=True)
    id_image = models.ImageField(upload_to=client_id_image_directory_path)

    # def get_update_url(self):
    #     return reverse("clients:client-id-update", kwargs={"id": self.id})

    def __str__(self):
        return self.id_number
