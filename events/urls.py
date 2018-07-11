from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventPageView.as_view(), name='events'),
]
