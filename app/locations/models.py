from django.db import models
from mixins.assets import TimeStampMixin


class District(TimeStampMixin):
    """
    District model
    """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# class Quarter(TimeStampMixin):
#     """
#     Quarter model
#     """
#     name = models.CharField(max_length=255)
#     district = models.ForeignKey(District, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name + ' - ' + self.district.name