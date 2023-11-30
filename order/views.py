from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.contrib import messages
from order.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Categories, Product, Cart, CartItems, Checkout, PaymentMethod
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.db import transaction

def index(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
        cart_items = CartItems.objects.filter(cart_id__in =cart )
        return render(request, 'order/index.html', {'categories': categories, 'products': products,"cart_count":cart_items.count()})
    else:
        return render(request, 'order/index.html', {'categories': categories, 'products': products})

def category_products(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    categories = Categories.objects.all()
    products = Product.objects.filter(category_name=category)
    return render(request, 'order/index.html', {'category': category, 'categories': categories, 'products': products})


def menu(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
    cart_items = CartItems.objects.filter(cart_id__in =cart )
    return render(request, 'order/menu.html', {'categories': categories, 'products': products, "cart_count":cart_items.count()})


def about(request):
    cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
    cart_items = CartItems.objects.filter(cart_id__in =cart )
    return render(request, 'order/about.html' , {"cart_count":cart_items.count()})


@login_required
def profile(request):
        user_profile = User.objects.get(username=request.user.username)
        cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
        cart_items = CartItems.objects.filter(cart_id__in =cart )
        return render(request, 'order/profile.html', {'user_profile': user_profile , "cart_count":cart_items.count()})



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
    cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
    cart_items = CartItems.objects.filter(cart_id__in =cart )
    if request.method == 'GET':
        return render(request, 'order/book.html', {"cart_count":cart_items.count()})  

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
    cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
    cart_items = CartItems.objects.filter(cart_id__in =cart )
    if request.method == 'POST':
        old_password = request.POST.get('password')
        new_password1 = request.POST.get('new_password')
        new_password2 = request.POST.get('cf_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrrect')
            return render(request, 'order/resetter.html', {"cart_count":cart_items.count()})

        if new_password1 == new_password2:
            request.user.set_password(new_password1)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('order:profile')

        else:
            messages.error(request, 'New passwords do not match')
            return render(request, 'order/resetter.html', {"cart_count":cart_items.count()})


    if request.method == 'GET':
     return render(request, 'order/resetter.html', {"cart_count":cart_items.count()})

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
    query = request.GET.get('query', '')
    cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
    cart_items = CartItems.objects.filter(cart_id__in =cart )
    if query:
        products = Product.objects.filter(Q(product_name__icontains=query) | Q(product_price=query))

        if products.exists():
            return render(request, 'order/searchmenu.html', {'products': products, 'query': query, "cart_count":cart_items.count()})
        else:
            messages.error(request, "OOPS! No item is found")
            return render(request, 'order/index.html', {'query': query, "cart_count":cart_items.count()})
    else:
        return redirect('/order/menu')

def productdetails(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.filter(user=request.user).values_list("id",flat=True)
    cart_items = CartItems.objects.filter(cart_id__in =cart )
    return render(request, 'order/productdetails.html', {'product': product, "cart_count":cart_items.count()})




@csrf_exempt
@require_POST
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        redirect_url = reverse('order:menu')

        # Your delete logic here
        product.delete()

        return JsonResponse({'message': 'Product deleted successfully.', 'redirect_url': redirect_url}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user, is_paid=False)
    cart_items = CartItems.objects.filter(cart=cart)
    total_price = sum(float(product.get_total_price()) for product in cart_items)
    subtotal = sum(float(product.get_total_price()) for product in cart_items)

    tax_rate = 0.05 
    shipping_cost = 15.00 
    tax = round(subtotal * tax_rate, 2)
    grand_total = subtotal + tax + shipping_cost

    return render(request, 'order/cart.html', { 'cart_items': cart_items,'cart_count': cart_items.count(), 'total_price': total_price, 'subtotal': subtotal, 'tax': tax, 'shipping_cost': shipping_cost, 'grand_total': grand_total})


@transaction.atomic
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    user = User.objects.get(id=request.user.id)

    
    with transaction.atomic():
        carts = Cart.objects.select_for_update().filter(user=user, is_paid=False)

    if carts.exists():
        cart = carts.first()
        cart_item = CartItems.objects.filter(cart=cart, product=product).first()

        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItems.objects.create(cart=cart, product=product)
    else:
        cart = Cart.objects.create(user=user, is_paid=False)
        CartItems.objects.create(cart=cart, product=product)

    
    messages.success(request, "Your food item is added into the cart!")
    return redirect('order:cart')



def removeitems(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        user = request.user

        carts = Cart.objects.filter(user=user, is_paid=False)

        if carts.exists():
            cart = carts.first()

            cart_item = CartItems.objects.filter(cart=cart, product=product).first()

            if cart_item:
                cart_item.delete()
                messages.success(request, "Your food item is removed from the cart!")
            else:
                messages.error(request, "The selected food item is not in the cart.")
        else:
            messages.error(request, "There is no active cart for the user.")

    return redirect('order:cart')


def update_cart(request):

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.quantity = quantity
        cart_item.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user, is_paid=False)
    cart_items = CartItems.objects.filter(cart=cart)
    
    if not cart_items:
        messages.error(request, 'Your shopping cart is empty.')
        return redirect('order:cart')

    subtotal = sum(float(item.get_total_price()) for item in cart_items)
    tax_rate = 0.05
    shipping_cost = 15.00
    tax = round(subtotal * tax_rate, 2)
    grand_total = subtotal + tax + shipping_cost

    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        address = request.POST.get('address')
        address_location = request.POST.get('address_location')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        payment_method = request.POST.get('payment_method')
        # Create a Checkout instance
        checkout = Checkout.objects.create(
            user=request.user,
            cart=cart,
            email=email,
            name=name,
            address=address,
            address_location=address_location,
            city=city,
            state=state,
            zip_code=zip_code,
           
        )

        if payment_method:
            PaymentMethod.objects.create( checkout=checkout, payment_method=payment_method)

        cart.is_paid = True
        cart.save()

        
        cart_items.delete()

        messages.success(request, 'Order placed successfully!')
        return redirect('order:index')  
    else:
        return render(request, 'order/checkout.html', {'cart_items': cart_items, 'subtotal': subtotal, 'tax': tax,
            'shipping_cost': shipping_cost, 'grand_total': grand_total})