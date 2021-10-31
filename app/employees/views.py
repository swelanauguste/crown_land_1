from django.shortcuts import render
from django.views.generic import UpdateView

from .models import Employee

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'middle_name', 'phone', 'bio']
    template_name_suffix = '_update_form'
    
  