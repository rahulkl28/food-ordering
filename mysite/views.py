from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')