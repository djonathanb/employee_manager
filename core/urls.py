"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework.urls import url

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/schema/', views.api_schema_view, name='api-docs-schema'),
    path('api/docs/', views.api_ui_view, name='api-docs-ui'),
    url(r"^api/", include('employee.urls')),
]
