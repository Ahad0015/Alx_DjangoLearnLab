"""
URL configuration for tm_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# Root URLConf (kind of the entry point for all routes)
urlpatterns = [
    # Django's built-in admin site
    path("admin/", admin.site.urls),

    # My tasks app (probably where most stuff will go for now)
    path("", include("tasks.urls")),   # maybe should namespace this later?

    # Auth routes (login/logout/password mgmt)
    # NOTE: might customize these templates later...
    path("accounts/", include("django.contrib.auth.urls")),

    # path("debug/", include("debug_toolbar.urls")),  # leaving this here in case I need it
]
