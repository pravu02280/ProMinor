from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


# Create your models here.
class RLeave(models.Model):
    subject = models.CharField(
        max_length=200, help_text="Enter a leave form")
    leavedate = models.DateField(null=True, blank=True)
    description = models.CharField(
        max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.subject


class RProgress(models.Model):
    subject = models.CharField(
        max_length=200, help_text="Enter a progress form")
    description = models.CharField(
        max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.subject
