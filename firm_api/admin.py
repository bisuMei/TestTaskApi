from django.contrib import admin
from .models import Employee, Boss, EmployeeSalary, Position
# Register your models here.

admin.site.register(Employee)
admin.site.register(Boss)
admin.site.register(EmployeeSalary)
admin.site.register(Position)

