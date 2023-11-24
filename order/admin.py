from django.contrib import admin
from .models import Contact, Product, Categories, Cart, CartItems

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Cart)
admin.site.register(CartItems)

