from django.db import models
from django.urls import reverse

# Create your models here.


class Boss(models.Model):
    boss_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.surname


class Position(models.Model):
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.position


class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="emp_position")
    employment_date = models.DateField()
    salary = models.IntegerField(blank=True)
    boss_id = models.ForeignKey(Boss, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('firm_api:details')


class EmployeeSalary(models.Model):
    total_salary = models.IntegerField(blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emp_salary')








