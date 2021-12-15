from django.urls import path

from . import views

app_name = "applications"


urlpatterns = [
    path(
        "", views.IndividualApplicationCreateView.as_view(), name="individual-application-create"
    ),
]
