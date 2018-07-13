from django.urls import path, include

from . import views

urlpatterns = [
    path('attendenceform/', views.attendenceformview, name='attendenceformview'),
]
