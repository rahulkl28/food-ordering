from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request, 'order/index.html')

def menu(request):
    return render(request,'order/menu.html')

def about(request):
    return render(request, 'order/about.html')


def book(request):
    if request.method == 'GET':
        return render(request, 'order/book.html')  

    if request.method == 'POST':

        if not request.POST.get("f_name"):
            messages.error(request, "Please enter you name")
            return redirect('order:book')
        
        if not request.POST.get("email"):
            messages.error(request, "Please enter you email")
            return redirect('order:book')
        
        if not request.POST.get("number"):
            messages.error(request, "Please enter you phone number")
            return redirect('order:book')
        
        if not request.POST.get("person"):
            messages.error(request, "Please enter the number of persons")
            return redirect('order:book')


        contact = Contact.objects.create(
            your_name = request.POST.get("f_name"),
            phone_number = request.POST.get("number"),
            your_email = request.POST.get("email"),
            persons_number = request.POST.get("person"),
            your_message = request.POST.get("message")
        )

        messages.success(request, "Your Booking is confirmed")
        return redirect('order:index')


def signup(request):
    if request.method == 'POST':

        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Check for errorneous inputs
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/order')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/order')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/order')


        #check the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('/order')

    else:
        return HttpResponse('404 - Not Found')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/order')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/order')


def logout(request):
    return