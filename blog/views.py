from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Welcome to the blog home</h1>')


def about(request):
    return HttpResponse('<h2>This is the about page<h2>')

