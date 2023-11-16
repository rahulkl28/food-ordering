from django.db import models
from autoslug import AutoSlugField
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
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
    product_price = models.CharField(max_length=10,null=True)
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
   
