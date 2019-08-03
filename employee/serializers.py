from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')


class EmployeeListSerializer(EmployeeSerializer):
    department = serializers.ReadOnlyField(source='department.name')
