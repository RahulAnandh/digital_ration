from django.db import models

# Create your models here.
class Admin_tb(models.Model):
    name = models.CharField(max_length=200,null='empty')
    email = models.CharField(max_length=200,null='empty')
    password = models.TextField(null='empty')
    
class User_registration_tb(models.Model):
    name = models.CharField(max_length=200,null='empty')
    email = models.CharField(max_length=200,null='empty')
    password = models.TextField(null='empty')
    phone = models.CharField(max_length=200,null='empty')
    gender = models.CharField(max_length=200,null='empty')
    aadharnumber = models.CharField(max_length=200,null='empty')
    rationcardnumber = models.CharField(max_length=200,null='empty')
    verified = models.BooleanField(default='False')

class Contact_tb(models.Model):
    name = models.CharField(max_length=200,null='empty')
    phone = models.CharField(max_length=200,null='empty')
    email = models.CharField(max_length=200,null='empty')
    subject = models.CharField(max_length=200,null='empty')
    message = models.CharField(max_length=300,null='empty')

class Subscribe_tb(models.Model):
    email = models.CharField(max_length=200,null='empty')

class Product_tb(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200,null='empty')
    price = models.CharField(max_length=20,null='empty')
    quantity = models.CharField(max_length=20,null='empty')
    discription = models.CharField(max_length=300,null='empty')
    
    
    