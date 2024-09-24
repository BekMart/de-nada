from django.urls import path
from . import views

urlpatterns = [
    path('', views.displaymenu , name='menu'),
]

