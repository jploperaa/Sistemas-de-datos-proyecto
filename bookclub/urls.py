from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", include("core.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout
    path("admin/", admin.site.urls),
    
]
