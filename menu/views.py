from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Beverages, Food

# Create your views here.
# class BeveragesList(generic.ListView):
#     queryset = Beverages.objects.all()
#     template_name = "menu/menu.html"

def displaymenu(request):
    print("About to render template")

    beverages = Beverages.objects.all()
    context = {'beverages': beverages}

    return render(
        request,
        "menu/menu.html",
        context
    )