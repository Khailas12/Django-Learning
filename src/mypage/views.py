from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user) # this shows the username in the terminal and shows anonymous in incognito mode
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, "home.html", {})

def content_view(request, *args, **kwargs):
    return render(request, "content.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about", {})