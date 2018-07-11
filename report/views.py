from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import LeaveForm, ProgressForm


def leaveformview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = LeaveForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return HttpResponseRedirect('/report/leaveform/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LeaveForm()

    return render(request, 'name.html', {'form': form})


def progressformview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = ProgressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            progress = form.save(commit=False)
            progress.user = request.user
            progress.save()
            return HttpResponseRedirect('/report/progressview/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProgressForm()

    return render(request, 'nameone.html', {'form': form})
