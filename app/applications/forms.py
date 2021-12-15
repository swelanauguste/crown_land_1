from django import forms
from django.forms import widgets

from .models import IndividualApplication


class IndividualApplicationCreateForm(forms.ModelForm):

    class Meta:
        model = IndividualApplication
        fields = "__all__"
        exclude = ['created_by', 'updated_by']

        widgets = {
            "application_type": widgets.CheckboxSelectMultiple(),
            "land_use": widgets.CheckboxSelectMultiple(),
            "easement": widgets.CheckboxSelectMultiple(),
            
        }

       
