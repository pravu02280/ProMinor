from django.urls import path, include

from . import views

urlpatterns = [
    path('leaveform/', views.leaveformview, name='leaveformview'),
    path('progressform/', views.progressformview, name='progressformview'),
]
