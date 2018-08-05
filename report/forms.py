from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms
from .models import RLeave, RProgress


class LeaveForm(forms.ModelForm):
    leavedate = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)
    class Meta:
        model = RLeave
        fields = ['leavedate', 'subject', 'description']


class ProgressForm(forms.ModelForm):
    class Meta:
        model = RProgress
        fields = ['subject', 'description']
