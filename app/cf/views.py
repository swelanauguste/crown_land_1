from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from clients.models import Client
from properties.models import Property

class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all().count()
        context['properties'] = Property.objects.all().count()
        return context
