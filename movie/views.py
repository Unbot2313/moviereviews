from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Greg Lim'})


def about(request):
    return HttpResponse('<h1>About Page</h1>')
