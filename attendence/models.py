from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Attendence(models.Model):
    date = models.DateField(null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.user.username
