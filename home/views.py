from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/home.html');

def menu(request):
    return render(request, 'pages/menu.html');