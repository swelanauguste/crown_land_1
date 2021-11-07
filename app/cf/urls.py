from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import DashBoardView

urlpatterns = [
    path("", DashBoardView.as_view(), name="dashboard"),
    path("employees/", include("employees.urls", namespace="employees")),
    path("clients/", include("clients.urls", namespace="clients")),
    path("properties/", include("properties.urls", namespace="properties")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
