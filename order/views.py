from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import Contact

def index(request):
    return render(request, 'order/index.html')

def menu(request):
    return render(request,'order/menu.html')

def about(request):
    return render(request, 'order/about.html')

def book(request):
    if request.method == 'GET':
        return render(request, 'order/book.html',)  
    if request.method == 'POST':

        if not request.POST.get("f_name"):
            return redirect('order:book')

        contact = Contact.objects.create(your_name = request.POST.get("f_name"),
            phone_number = request.POST.get("number"),
            your_email = request.POST.get("email"),
            persons_number = request.POST.get("person"),
            your_message = request.POST.get("message")
        )

        return redirect('order:index')