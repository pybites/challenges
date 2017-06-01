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
            render(request, 'app/apps.html',{'form':form})
            #return render(request, 'app/apps.html',{'form':form})
        else:
            print('invalid')
    else:
        form = CalcForm()
    return render(request, 'app/apps.html',{'form':form})

# def result(request):
#     return(request, 'app/result.html')
