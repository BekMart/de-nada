from django.shortcuts import render

# Create your views here.
def displaymenu(request):
    print("About to render template")

    return render(
        request,
        "menu/menu.html",
    )