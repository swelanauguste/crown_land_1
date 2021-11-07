from django import forms
from .models import Property


class PropertyCreateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
        exclude = ["created_by", "updated_by", "slug"]


class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
        exclude = ["created_by", "updated_by", "slug"]
