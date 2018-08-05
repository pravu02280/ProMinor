from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms
from .models import Attendence


class AttendenceForm(forms.ModelForm):
    date = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        years=((datetime.datetime.now().year,)),
        months=({1: datetime.datetime.now().strftime("%B")}),
        
    ),
    initial=datetime.date.today
)
    class Meta:
        model = Attendence
        fields = ['date']
