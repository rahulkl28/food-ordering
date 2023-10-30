from django.db import models

# Create your models here.
class Contact(models.Model):
    your_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    your_email = models.EmailField(null=True,blank=True)
    persons_number = models.IntegerField(null=True,blank=True)
    your_message = models.TextField(max_length=100,null=True,blank=True)