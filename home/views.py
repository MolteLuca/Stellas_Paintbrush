from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/entryPage.html')


def about(request):
    return render(request, 'home/mainPage.html', {'title': 'About'})

# Create your views here.
