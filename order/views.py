from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'order/index.html')

def menu(request):
    return render(request,'order/menu.html')

def about(request):
    return render(request, 'order/about.html')

def book(request):
    return render(request, 'order/book.html')