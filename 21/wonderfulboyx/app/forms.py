from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Calc

class CalcForm(forms.ModelForm):
    # device = forms.ModelChoiceField(queryset=Device.objects.all())
    class Meta:
         model = Calc
         fields = ('company', 'device','time')
         labels = {
            'time': _('Time(h)'),
         }
