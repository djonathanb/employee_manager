from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = 'department'


class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    class Meta:
        db_table = 'employee'
