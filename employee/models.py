from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'department'