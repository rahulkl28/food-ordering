from django.db import models
from autoslug import AutoSlugField
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Contact(models.Model):
    your_name = models.CharField(max_length=20,null=False,blank=True)
    phone_number = models.IntegerField(null=True,blank=True)
    your_email = models.EmailField(null=True,blank=True)
    persons_number = models.IntegerField(null=True,blank=True)
    your_message = models.TextField(max_length=200,null=True,blank=True)

 
class Categories(models.Model):
    Category = models.CharField(max_length=100, null=False, blank=False) 
    slug = AutoSlugField(populate_from='Category', unique=True, null=True, default=None)

    def __str__(self):
        return self.Category
   


class Product(models.Model):
    product_img = models.ImageField(null=False, blank=False)
    product_name = models.CharField(max_length=20,null=False,blank=True)
    product_desc = models.CharField(max_length=200,null=True,blank=True)
    product_price = models.CharField(max_length=200, null=True,blank=True)
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE, default=True, null=False)

    

class User(AbstractUser):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, null=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    pass_word = models.CharField(max_length=100, null= True,blank=False)

    class Meta:
        managed = True
        db_table = "tbl_user"
   


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    is_paid = models.BooleanField(default=False)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product , on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_total_price(self):
        return float(self.quantity) * float(self.product.product_price)
    

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkout")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart")
    email = models.EmailField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    address_location = models.TextField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)


class PaymentMethod(models.Model):
    checkout = models.OneToOneField(Checkout,  on_delete=models.CASCADE, related_name="checkout")
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card')], default='credit_card')