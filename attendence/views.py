import datetime
import calendar

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import AttendenceForm
from .models import Attendence


def attendenceformview(request, format=None):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = AttendenceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            attendence = form.save(commit=False)
            attendence.user = request.user
            attendence.date = datetime.date.today()
            attendence.save()
            return HttpResponseRedirect('/attendence/attendenceform/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AttendenceForm()

    return render(request, 'name1.html', {'form': form})


def salary_view(request):
    first_day_of_month = datetime.date.today().replace(day=1)
    total_salary = Attendence.objects.filter(user=request.user).filter(date__gte=first_day_of_month).filter(date__lte=first_day_of_month.replace(day=calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]))
    salary = total_salary.count() * 100
    return render(request, 'salary_details.html')
