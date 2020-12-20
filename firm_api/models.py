from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Boss(models.Model):
    boss_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return str(self.boss_id)


class Position(models.Model):
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.position


class HierarchyLevels(models.Model):
    level = models.PositiveIntegerField(unique=True)

    def save(self, *args, **kwargs):
        if self.level > 5:
            return "Maximum 5 levels"
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        lev = str(self.level)
        return lev


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="emp_position")
    employment_date = models.DateField()
    salary = models.IntegerField(blank=True)
    total_salary_paid = models.IntegerField(null=True)
    boss_id = models.ForeignKey(Boss, on_delete=models.CASCADE, related_name='emp_boss_id')
    hierarchy_level = models.ForeignKey(HierarchyLevels, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.last_name













