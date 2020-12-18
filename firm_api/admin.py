from django.contrib import admin
from .models import Employee, Boss, Position, HierarchyLevels
# Register your models here.
from django_admin_relation_links import AdminChangeLinksMixin


def delete_total_paid(modeladmin, request, queryset):
    new = 0
    for employee in queryset:
        employee.total_salary_paid = new
        employee.save()




delete_total_paid.short_description = "Delete chosen salaries"


@admin.register(Boss)
class BossAdmin(AdminChangeLinksMixin, admin.ModelAdmin):

    list_display = ['boss_id']

    changelist_links = ['emp_boss_id']


@admin.register(Employee)
class EmployeeAdmin(AdminChangeLinksMixin, admin.ModelAdmin):

    list_display = ('first_name', 'middle_name', 'last_name',
                    'position', 'boss_id_link', 'salary', 'total_salary_paid')
    list_filter = ('position', 'hierarchy_level')
    change_links = ['boss_id']
    actions = [delete_total_paid]






admin.site.register(Position)
admin.site.register(HierarchyLevels)
