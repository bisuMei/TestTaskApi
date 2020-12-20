from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics

from .decorators import define_usage
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


# @authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
# @permission_classes((IsAdminUser,))
# class EmployeeList(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['hierarchy_level']











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


