from django.shortcuts import render
from django.http import HttpResponse


def entry(request):
    return render(request, 'home/entryPage.html')


def home(request):
    return render(request, 'home/mainPage.html', {'title': 'Homepage'})

# Create your views here.
