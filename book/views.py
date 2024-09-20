from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booktable(request):
    return HttpResponse("BOOK A TABLLE HERE!")