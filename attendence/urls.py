from django.urls import path, include

from . import views

urlpatterns = [
    path('attendenceform/', views.attendenceformview, name='attendenceformview'),
    path('salary/', views.salary_view, name='salaryview'),

]
