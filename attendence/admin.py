from django.contrib import admin
from .models import Attendence

# Register your models here.
@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'approve')
