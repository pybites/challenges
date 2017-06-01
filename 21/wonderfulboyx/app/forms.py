from django import forms
from .models import Calc

class CalcForm(forms.ModelForm):
    # device = forms.ModelChoiceField(queryset=Device.objects.all())
    class Meta:
         model = Calc
         fields = ('campany', 'device','time')
