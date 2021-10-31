from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    is_commissioner = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    is_clerk = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    middle_name = models.CharField(max_length=254, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=254)
    bio = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("employees:employee-update", kwargs={"slug": self.slug})

    def __str__(self):
        if self.first_name and self.last_name:
            return self.last_name + ", " + self.first_name
        return self.user
