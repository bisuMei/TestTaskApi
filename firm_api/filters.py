import django_filters
from .models import Employee
from django import forms
from django.contrib.auth.models import Group


class EmployeeFilter(django_filters.FilterSet):
    group = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
                                                      widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name',
                  'position', 'employment_date', 'salary',
                  'boss_id', 'group']















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


