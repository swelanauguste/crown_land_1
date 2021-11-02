from django.shortcuts import render
from django.views.generic import UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employee


class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employee
    fields = ["first_name", "last_name", "middle_name", "phone", "bio"]
    template_name_suffix = "_update_form"
    success_message = "Updated"

class EmployeeDetailView(DetailView):
    model = Employee
