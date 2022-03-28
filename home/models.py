from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categories(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name



class SubCategories(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=250)
    category=models.ForeignKey(categories,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.cat_name


class Shubimage(models.Model):
    name=models.CharField(max_length=100)
    s1=models.ImageField(upload_to="shop/product/subproducts")
    s2=models.ImageField(upload_to="shop/product/subproducts")
    s3=models.ImageField(upload_to="shop/product/subproducts")

    def __str__(self):
        return self.name
    

    
    
class product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    aprice=models.CharField(max_length=100)
    dprice=models.CharField(max_length=100)
    image=models.ImageField(upload_to="shop/product")
    shortdesc=models.TextField()
    longdesc=models.TextField()
    Brand=models.CharField(max_length=150)
    quant=models.IntegerField()
    date=models.DateField()
    rate=models.IntegerField(null=True,default=0)
    category= models.ForeignKey(categories, null=True, on_delete=models.SET_NULL)
    subcategory=models.ForeignKey(SubCategories,null=True,on_delete=models.SET_NULL)
    subimg=models.ForeignKey(Shubimage,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    password=models.CharField(max_length=250)
    address=models.TextField(null=True)
    dob=models.CharField(max_length=50,default=None)
    gender=models.CharField(max_length=100,default=None)
    postal_code=models.CharField(max_length=30)
    date_created=models.DateField()

    def __str__(self):
        return self.firstname


class order(models.Model):
    STATUS=[('Pending','Pending'),('Out for delivery','Out for delivery'),('Delivered','Delivered'),('Canceled','Canceled')]
    order_id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,default=None)
    email=models.CharField(max_length=100,default=None)
    address=models.CharField(max_length=300,default=None)
    city=models.CharField(max_length=50,default=None)
    state=models.CharField(max_length=100,default=None)
    Zip=models.CharField(max_length=20,default=None)
    order_date=models.DateField()
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.fullname


class templates(models.Model):
    imagename=models.CharField(max_length=250,default="")
    image=models.ImageField(upload_to="shop")

    def __str__(self):
        return self.imagename



