# from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Client, Title, ClientIdentification
from .forms import ClientUpdateForm, ClientCreateForm, ClientIdentificationUpdateForm
from django.db.models import Q
from django.views.generic.edit import FormMixin



class ClientSearch(LoginRequiredMixin, ListView):
    model = Client
    # template_name = "clients/client_search.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        if query:
            Clients = Client.objects.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(middle_name__icontains=query)
                | Q(occupation__icontains=query)
                | Q(phone__icontains=query)
                | Q(address__icontains=query)
                | Q(district__name__icontains=query)
                | Q(nationality__icontains=query)
            ).distinct()
            context["object_list"] = Clients
        else:
            context["object_list"] = Client.objects.all()
        return context


class ClientIdentificationUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, DetailView):
    model = Client
    form_class = ClientIdentificationUpdateForm
    template_name = "clients/client_identification_form.html"
    template_name_suffix = '_update_form'
    success_message = "Updated"

    def get_success_url(self):
        return reverse("clients:client-detail", args=(self.object.slug,))

    def get_initial(self):
        return {"identification": self.get_object()}


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.identification = self.object
        form.save()
        return super(ClientIdentificationUpdateView, self).form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    paginate_by = 10


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

