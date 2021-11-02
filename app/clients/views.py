# from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Client, Title, ClientIdentification
from .forms import ClientUpdateForm, ClientCreateForm


class ClientIdentificationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ClientIdentification
    fields = ["identification_type", "identification_number"]
    template_name = "clients/client_identification_form.html"
    success_message = "Created"

    def get_success_url(self):
        return reverse("client_detail", kwargs={"slug": self.object.client.slug})


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    paginate_by = 8


class ClientCreateView(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Client
    form_class = ClientCreateForm
    success_message = "Created"


    def get_success_url(self):
        return reverse("clients:client-update", args=(self.object.slug,))


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name_suffix = "_update_form"
    success_message = "Updated"

