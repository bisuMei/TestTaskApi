from django.shortcuts import render, get_object_or_404
from . import models
from .filters import EmployeeFilter
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from . import forms
from . import models

# Create your views here.


def index(request):
    return render(request, 'firm_api/index.html', {'title': 'Main page'})


def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Logged In')
                else:
                    return HttpResponse('Not active')
            else:
                return HttpResponse('Wrong credentials')
    else:
        form = forms.LoginForm()
        return render(request, 'training/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            models.Employee.objects.create(user=user)
            return redirect('/')
    else:
        form = forms.RegisterForm()
    return render(request, "registration/register.html", {'form': form})


def employee_details(request):
    employee = get_object_or_404(models.Employee, pk=id)
    return render(request,
                  'firm_api/details.html',
                  {'employee': employee})


def search(request):
    user_list = models.Employee.objects.all()
    user_filter = EmployeeFilter(request.GET, queryset=user_list)
    return render(request, 'firm_api/employees.html', {'filter': user_filter})
