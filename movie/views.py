from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Tomas Ramirez Galeano'})


def about(request):
    return render(request, 'about.html')
