from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms
from .models import Attendence


class AttendenceForm(forms.ModelForm):
    class Meta:
        model = Attendence
        fields = ['date', 'user']
