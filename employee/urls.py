from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urls import url

from . import views

router = DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)

urlpatterns = [
    url(r"", include(router.urls)),
]
