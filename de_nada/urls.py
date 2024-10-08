"""
URL configuration for de_nada project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import homepage
from book.views import booktable
from menu.views import displaymenu
from contact.views import contactpage

urlpatterns = [
    path('', homepage, name='home'),
    path('admin/', admin.site.urls),
    path('book/', booktable, name='book'),
    path('contact/', contactpage, name='contact'),
    path('menu/', displaymenu, name='menu'),
    path('summernote/', include('django_summernote.urls')),
]
