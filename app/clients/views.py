from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Client, Title
from .forms import ClientUpdateForm, ClientCreateForm


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    pagination = 10


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientCreateForm

    def get_success_url(self):
        return reverse('clients:client-update',args=(self.object.slug,))


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name_suffix = "_update_form"
