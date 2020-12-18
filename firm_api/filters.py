from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import generics

from .models import Employee
from django import forms
from django.contrib.auth.models import Group
from django_filters import rest_framework as filters

from .serializes import EmployeeSerializer


class EmployeeFilter(filters.FilterSet):
    level = filters.NumberFilter(field_name="level")

    fields = ['first_name', 'middle_name', 'last_name',
              'position', 'employment_date', 'salary',
              'boss_id', 'hierarchy_level', 'total_salary_paid']


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hierarchy_level']











# class PositionFilter(django_filters.FilterSet):
#
#     CHOICES = (
#         ('ascending', 'Ascending'),
#         ('descending', 'Descending')
#     )
#
#     ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')
#
#     class Meta:
#         model = Position
#         fields = {
#             'position': ['icontains'],
#         }
#
#     def filter_by_order(self, queryset, name, value):
#         expression = 'created' if value == 'ascending' else '-created'
#         return queryset.order_by(expression)


