from django_filters import rest_framework as filters


class EmployeeFilter(filters.FilterSet):
    level = filters.NumberFilter(field_name="level")

    fields = ['first_name', 'middle_name', 'last_name',
              'position', 'employment_date', 'salary',
              'boss_id', 'hierarchy_level', 'total_salary_paid']
