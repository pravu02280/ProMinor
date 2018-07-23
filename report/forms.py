from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms
from .models import RLeave, RProgress


class LeaveForm(forms.ModelForm):
    class Meta:
        model = RLeave
        fields = ['subject', 'description', 'leavedate']


class ProgressForm(forms.ModelForm):
    class Meta:
        model = RProgress
        fields = ['subject', 'description']
