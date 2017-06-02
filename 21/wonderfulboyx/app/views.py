from django.shortcuts import render
from .models import *

def apps(request):
    from .forms import CalcForm
    if request.method == 'POST':
        print('hi')
        form = CalcForm(request.POST)
        if form.is_valid():
            print('valid')
            form = form.save()
            cost = form.cost
        else:
            print('invalid')
    else:
        cost = 0
    form = CalcForm()
    return render(request, 'app/apps.html',{'form':form ,'cost':cost,'calc':Calc.objects.all()})
# def result(request):
#     return(request, 'app/result.html')

def show(request):
    return render(request, 'app/show.html',{'calc':Calc.objects.all()})
