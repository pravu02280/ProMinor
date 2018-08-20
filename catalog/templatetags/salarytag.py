import datetime
from django import template

from attendence.models import Attendence
import datetime
import calendar

register = template.Library()

@register.simple_tag(takes_context=True)
def salarytag(context):
    request = context["request"]
    first_day_of_month = datetime.date.today().replace(day=1)
    total_salary = Attendence.objects.filter(user=request.user).filter(date__gte=first_day_of_month).filter(date__lte=first_day_of_month.replace(day=calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]))
    salary = total_salary.count() * 100
    return salary
