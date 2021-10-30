from django.db import models
from django.contrib.auth.models import AbstractUser


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
    phone = models.CharField(max_length=254)
    bio = models.TextField(blank=True)
    
    

    def __str__(self):
        if self.first_name and self.last_name:
            return self.last_name + ', ' + self.first_name
        return self.user