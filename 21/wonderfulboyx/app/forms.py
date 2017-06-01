from django import forms
from .models import Device, Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('user','device','time','cost')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
