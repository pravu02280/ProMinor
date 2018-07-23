from django.contrib import admin
from .models import RLeave, RProgress

# Register your models here.
admin.site.register(RProgress)


@admin.register(RLeave)
class RleaveAdmin(admin.ModelAdmin):
    list_display = ('subject', 'leavedate', 'approve', 'user')
