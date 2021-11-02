from django.contrib import admin

from .models import Client, Title, ClientIdentification

admin.site.register(Client)
admin.site.register(Title)
admin.site.register(ClientIdentification)
