from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import Calc, Company, Device

class CalcForm(forms.ModelForm):
    # device = forms.ModelChoiceField(queryset=Device.objects.all())
    class Meta:
         model = Calc
         fields = ('company', 'device','time')
         labels = {
            'time': _('Time(h)'),
         }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name','charge')
        labels = {
           'charge': _('Charge(/kWh)'),
        }

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('name','consumption')
        labels = {
           'consumption': _('Consumption(W)'),
        }
