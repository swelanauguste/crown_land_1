from django import forms

from .models import Client, ClientIdentification


class ClientIdentificationUpdateForm(forms.ModelForm):
    class Meta:
        model = ClientIdentification
        fields = ("identification", "form_of_id", "id_number", "id_image")
        widgets = {"identification": forms.HiddenInput()}


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
        fields = ["title","first_name", "last_name", "phone"]
