from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.contrib import messages
from order.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Categories, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash



def index(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    return render(request, 'order/index.html', {'categories': categories, 'products': products})

def category_products(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    categories = Categories.objects.all()
    products = Product.objects.filter(category_name=category)
    return render(request, 'order/index.html', {'category': category, 'categories': categories, 'products': products})


def menu(request):
    return render(request,'order/menu.html')


def about(request):
    return render(request, 'order/about.html')


@login_required
def profile(request):
        user_profile = User.objects.get(username=request.user.username)
        return render(request, 'order/profile.html', {'user_profile': user_profile})



@login_required
def delete_data(request):

    if request.method == 'POST':

        user = User.objects.get(id=request.user.id)

        if 'fname' in request.POST:
            user.first_name = " "
            messages.success(request, 'First name deleted succesfully')


        if 'lname' in request.POST:
            user.last_name = " "
            messages.success(request, 'Last name deleted succesfully')

        if 'email' in request.POST:
            user.email = " "
            messages.success(request, 'Email deleted succesfully')

        user.save()
        return redirect("order:profile")


@login_required
def update_data(request):
    if request.method == 'POST':

        user = User.objects.get(id = request.user.id)
        if request.POST.get("username"):
            user.username = request.POST.get("username")
        if request.POST.get("fname"):
            user.first_name = request.POST.get("fname")
        if request.POST.get("lname"):
            user.last_name = request.POST.get("lname")
        if request.POST.get("email"):
            user.email = request.POST.get("email")
        user.save()
        return redirect("order:profile")

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


def resetter(request):
    if request.method == 'POST':
        old_password = request.POST.get('password')
        new_password1 = request.POST.get('new_password')
        new_password2 = request.POST.get('cf_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrrect')
            return render(request, 'order/resetter.html')

        if new_password1 == new_password2:
            request.user.set_password(new_password1)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('order:profile')

        else:
            messages.error(request, 'New passwords do not match')
            return render(request, 'order/resetter.html')


    if request.method == 'GET':
     return render(request, 'order/resetter.html')

def signup(request):
    if request.method == 'POST':

        if not  request.POST['username'].isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/order')
        if (request.POST['pass1']!= request.POST['pass2']):
             messages.error(request, " Passwords do not match")
             return redirect('/order')

        #check the user
        myuser = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['pass1'],
            first_name=request.POST['fname'],
            last_name=request.POST['lname']
        )

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

    return HttpResponse("404- Not found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/order')


def searchmenu(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query:
            products = Product.objects.filter(product_name__icontains=query)
            return render(request, 'order/searchmenu.html', {'products': products})
        
        else:
            messages.error(request, "OOPS! No item is found")
            return redirect('/order')

