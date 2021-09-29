from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # this shows the username in the terminal and shows anonymous in incognito mode
    print(request.user)
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})
