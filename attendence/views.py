from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import AttendenceForm


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
            attendence.save()
            return HttpResponseRedirect('/attendence/attendenceform/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AttendenceForm()

    return render(request, 'name.html', {'form': form})
