from django.urls import path

from . import views

app_name = "properties"


urlpatterns = [
    path("", views.PropertyListView.as_view(), name="property-list"),
    path("search", views.PropertySearch.as_view(), name="property-search"),
    path("create", views.PropertyCreateView.as_view(), name="property-create"),
    path(
        "property/detail/<slug:slug>", views.PropertyDetailView.as_view(), name="property-detail"
    ),
    path(
        "property/update/<slug:slug>", views.PropertyUpdateView.as_view(), name="property-update"
    ),
]
