from django.urls import path

from . import views

app_name = "clients"


urlpatterns = [
    path("", views.ClientListView.as_view(), name="client-list"),
    path("search/", views.ClientSearch.as_view(), name="client-search"),
    path("detail/<slug:slug>/", views.ClientDetailView.as_view(), name="client-detail"),
    path("create", views.ClientCreateView.as_view(), name="client-create"),
    path("update/<slug:slug>/", views.ClientUpdateView.as_view(), name="client-update"),
    path(
        "update/client/id-info/<slug:slug>",
        views.ClientIdentificationUpdateView.as_view(),
        name="client-id-update",
    ),
]
