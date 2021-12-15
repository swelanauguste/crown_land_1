from django.shortcuts import render

from django.views.generic import CreateView


from .models import IndividualApplication
from .forms import IndividualApplicationCreateForm


class IndividualApplicationCreateView(CreateView):
    model = IndividualApplication
    form_class = IndividualApplicationCreateForm
