from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'order/index.html')


