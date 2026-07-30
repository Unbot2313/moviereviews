from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Tomas Ramirez Galeano'})


def about(request):
    return HttpResponse('<h1>About Page</h1>')
