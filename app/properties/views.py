from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Property
from .forms import PropertyCreateForm, PropertyUpdateForm


class PropertySearch(LoginRequiredMixin, ListView):
    model = Property
    # template_name = "clients/client_search.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        if query:
            properties = Property.objects.filter(
                Q(block__icontains=query)
                | Q(parcel__icontains=query)
                | Q(slug__icontains=query)
                | Q(address__icontains=query)
                | Q(district__name__icontains=query)
            ).distinct()
            context["object_list"] = properties
        else:
            context["object_list"] = Property.objects.all()
        return context


class PropertyListView(ListView):
    model = Property
    ordering = ["-created_at"]


class PropertyDetailView(DetailView):
    model = Property


class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyUpdateForm
    template_name_suffix = "_update_form"


class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyCreateForm