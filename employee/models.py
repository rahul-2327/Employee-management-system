from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    # department = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)
    # date_joined = models.DateField(auto_now_add=True)
    # salary = models.DecimalField(max_digits=10, decimal_places=2)
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        # return f"{self.first_name} {self.last_name}"
        return f"id: {self.employee_id} | name: {self.employee_name}"
