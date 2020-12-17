from django.shortcuts import render, get_object_or_404
from . import models
from .filters import PositionFilter
# Create your views here.


def index(request):
    return render(request, 'firm_api/index.html', {'title': 'Main page'})


def all_employees(request):
    employees_list = models.Employee.objects.all()
    filter = PositionFilter(request.GET, queryset=models.Position.objects.all())
    return render(request,
                  'firm_api/employees.html',
                  {'employees': employees_list,
                   'filter': filter})


def employee_details(request):
    employee = get_object_or_404(models.Employee, pk=id)
    return render(request,
                  'firm_api/details.html',
                  {'employee': employee})


