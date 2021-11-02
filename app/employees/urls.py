from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    path(
        "update/<slug:slug>", views.EmployeeUpdateView.as_view(), name="employee-update"
    ),
    path(
        "detail/<slug:slug>", views.EmployeeDetailView.as_view(), name="employee-detail"
    ),
]
