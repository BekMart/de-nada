from django.urls import path
from . import views
from django.template import loader

urlpatterns = [
    path('', views.booktable , name='book'),
]