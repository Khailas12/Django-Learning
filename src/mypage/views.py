from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    # this shows the username in the terminal and shows anonymous in incognito mode
    print(request.user)
    # return HttpResponse('<h1>Hello World</h1>')
    context = {}
    return render(request, "home.html", context)


def contact_view(request, *args, **kwargs):
    context = {
        "name": "Bruce Wayne",
        "age": 20,
        "place": "Gotham",
        "number": 1234567890,
        "companies": ["wayne aerospace", "wayne aviation", "wayne biotech", "wayne construction"]

    }
    return render(request, "contact.html", context)


def about_view(request, *args, **kwargs):
    context = {
        "my_text": "Django Learning",
        "this_is_true": True,
        "my_number": 12345,
        "my_list": [234, 456, 789, 'abc']
    }
    return render(request, "about.html", context)


def practice_view(request, *args, **kwargs):
    context = {
        "title": "django",
        "blah": "whatever",
        "other": "cool",
        "num": 321,
        "listing": ["kfdbke", "lbsfdibd", 9834, "febbfi"],
        "my_html": "<h1>hello world</h1>"
    }
    return render(request, 'practice.html', context)