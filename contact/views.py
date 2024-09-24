from django.shortcuts import render

# Create your views here.
def contactpage(request):
    print("About to render template")

    return render(
        request,
        "contact/contact.html",
    )