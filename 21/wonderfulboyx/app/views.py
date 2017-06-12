from django.shortcuts import render
from .models import *
from .forms import *

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form = form.save()
    form = CompanyForm()
    return render(request, 'app/create_company.html',{'form':form, 'company':Company.objects.all()})

def create_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form = form.save()
    form = DeviceForm()
    return render(request, 'app/create_device.html',{'form':form, 'device':Device.objects.all()})

def apps(request):
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            form = form.save()
            cost = form.cost
    else:
        cost = 0
    form = CalcForm()
    return render(request, 'app/apps.html',{'form':form ,'cost':cost})

def show(request):
    return render(request, 'app/show.html',{'calc':Calc.objects.all()})
