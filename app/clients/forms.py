from django import forms

from .models import Client


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ["created_by", "updated_by", "slug"]
        # widgets = {
        #     'phone': forms.TextInput(attrs={'class': 'w-1/2'}),
        # }


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name"]
