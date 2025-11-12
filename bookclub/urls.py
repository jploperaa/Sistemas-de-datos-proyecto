# bookclub/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Django login/logout/register pages
    path('accounts/', include('django.contrib.auth.urls')),

    # ✅ Your app
    path('', include('core.urls')),
]
