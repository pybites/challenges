from django.shortcuts import render
from .models import *

def apps(request):
    devices = Device.objects.all()
    return render(request, 'app/apps.html',{'devices':devices})

from django.http import HttpResponseRedirect
from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'app/name.html', {'form': form})
