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

class Subscribers_tb(models.Model):
    email = models.CharField(max_length=200,null='empty')

class Product_tb(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200,null='empty')
    price = models.CharField(max_length=20,null='empty')
    quantity = models.CharField(max_length=20,null='empty')
    discription = models.CharField(max_length=300,null='empty')
    month = models.CharField(max_length=20,null='empty')

class  Notification_tb(models.Model):
    notificationtype = models.CharField(max_length=30,null='empty')
    date = models.CharField(max_length=20,null='empty')
    message = models.CharField(max_length=20,null='empty')
    read = models.BooleanField(default='False')

class  Kart_tb(models.Model):
    userid=models.ForeignKey(User_registration_tb,on_delete=models.CASCADE)
    productid=models.ForeignKey(Product_tb,on_delete=models.CASCADE)
    productcount = models.CharField(max_length=10)
   
    
    
    