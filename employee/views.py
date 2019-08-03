from rest_framework import viewsets

from . import serializers
from .models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EmployeeListSerializer
        return serializers.EmployeeSerializer
