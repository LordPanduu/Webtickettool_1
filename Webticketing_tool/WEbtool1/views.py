from typing import Dict, List

from django.shortcuts import render
from django.http import request, HttpResponse

tickets = [
    {
        "author": "Elias",
        "title": "network connection failed",
        "content": "I cant connect to the server share",
        "post_date": "18.11.2020"
    },
    {
        "author": "Elias",
        "title": "network connection failed",
        "content": "I cant connect to the server ",
        "post_date": "18.11.2020"
    }
]


# Create your views here.
def hi(request):
    return render(request, "Webtool/hi.html")


def login(request):
    return render(request, 'Login/login.html')


def dashboard(request):
    context = {
        'tickets': tickets
    }
    return render(request, 'Dashboard/skel_js/dashboard.html', context)


