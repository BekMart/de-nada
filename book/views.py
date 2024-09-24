from django.shortcuts import render

# Create your views here.
def booktable(request):
    print("About to render template")

    return render(
        request,
        "book/book.html",
    )