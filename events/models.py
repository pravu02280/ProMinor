from django.db import models


# Create your models here.
class Event(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the Event")

    def __str__(self):

        return self.title
