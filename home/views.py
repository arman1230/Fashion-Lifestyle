from asyncio.windows_events import NULL
import http
from http.client import HTTPResponse
from math import prod
from pickle import GET
import re
from unicodedata import category, name
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import SubCategories, categories, customer, order,product, Shubimage,templates
from datetime import datetime
import random
import json

# Create your views here.
#@login_required(login_url="/login")
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    log=templates.objects.get(pk=1)
    user=templates.objects.get(pk=2)
    womens=templates.objects.get(pk=3)
    mens=templates.objects.get(pk=4)
    carousel=templates.objects.get(pk=5)
    cart=templates.objects.get(pk=6)
    home=templates.objects.get(pk=7)
    shoe=product.objects.filter(subcategory=2)
    prodshirt=product.objects.filter(subcategory=3)
    lshoes=product.objects.filter(subcategory=9)
    lshirt=product.objects.filter(subcategory=10)
    prod=product.objects.all()
    tmp=list(prod)[:]
    random.shuffle(tmp)
    return render(request,'home.html',{'prod':tmp,'logo':log,'user':user,'womens':womens,'mens':mens,
    'carousel':carousel,'cart':cart,'home':home,'shoe':shoe,'prodshirt':prodshirt,
    'lshoes':lshoes,'lshirt':lshirt})

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pswd=request.POST.get("pswd")
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            login(request,user)
            messages.success(request,"You successfully logged in")
            return redirect("/")
        else:
            messages.warning(request,"   Your creadentials are not matched")
        # cust=customer.objects.get(username=uname)
        # if cust.password == pswd:
        #     return redirect("/")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("/login")
def signin(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        # phone=request.POST.get("phone")
        # dob=request.POST.get("dob")
        # gender=request.POST.get("gender")
        # address=request.POST.get("tarea")
        # pcode=request.POST.get("pcode")
        uname=request.POST.get("uname")
        pswd=request.POST.get("pass")
        pswd1=request.POST.get("pass1")
        print(fname,lname,uname,pswd,pswd1)
        if(pswd==pswd1 and uname!="" and pswd!="" and fname!="" and lname!="" and email!=""):
            myuser=User.objects.create_user(uname,email,pswd)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            return redirect("/")
        # cust = customer(firstname=fname,lastname=lname,email=email,phone=phone,dob=dob,gender=gender,address=address,postal_code=pcode,username=uname,password=pswd,date_created=datetime.today())
        # cust.save()
            
            
    return render(request,'sign1.html')

def mens(request):
    log=templates.objects.get(pk=1)
    user=templates.objects.get(pk=2)
    womens=templates.objects.get(pk=3)
    mens=templates.objects.get(pk=4)
    carousel=templates.objects.get(pk=5)
    cart=templates.objects.get(pk=6)
    home=templates.objects.get(pk=7)
    shoe=product.objects.filter(subcategory=2)
    prodshirt=product.objects.filter(subcategory=3)
    prodtshirt=product.objects.filter(subcategory=1)
    prodwatch=product.objects.filter(subcategory=4)
    prodjeans=product.objects.filter(subcategory=5)
    categories=SubCategories.objects.filter(category=1)

    context={'logo':log,'user':user,'womens':womens,'mens':mens,
    'carousel':carousel,'cart':cart,'home':home,'shoe':shoe,'prodshirt':prodshirt,'prodtshirt':prodtshirt,'prodwatch':prodwatch,'prodjeans':prodjeans,
    'categories':categories,'cat':request.POST.get("flexRadioDefault")}

    return render(request,'mens.html',context)


def womens(request):
    log=templates.objects.get(pk=1)
    user=templates.objects.get(pk=2)
    womens=templates.objects.get(pk=3)
    mens=templates.objects.get(pk=4)
    carousel=templates.objects.get(pk=5)
    cart=templates.objects.get(pk=6)
    home=templates.objects.get(pk=7)
    shoe=product.objects.filter(subcategory=9)
    prodshirt=product.objects.filter(subcategory=10)
    kurtis=product.objects.filter(subcategory=8)
    prodjeans=product.objects.filter(subcategory=6)
    categories=SubCategories.objects.filter(category=1)

    context={'logo':log,'user':user,'womens':womens,'mens':mens,
    'carousel':carousel,'cart':cart,'home':home,'shoe':shoe,'prodshirt':prodshirt,'kurtis':kurtis,'prodjeans':prodjeans,
    'categories':categories,'cat':request.POST.get("flexRadioDefault")}

    return render(request,'womens.html',context)


def kids(request):
    log=templates.objects.get(pk=1)
    user=templates.objects.get(pk=2)
    womens=templates.objects.get(pk=3)
    mens=templates.objects.get(pk=4)
    carousel=templates.objects.get(pk=5)
    cart=templates.objects.get(pk=6)
    home=templates.objects.get(pk=7)
    shoe=product.objects.filter(subcategory=12)
    prodshirt=product.objects.filter(subcategory=11)
    watch=product.objects.filter(subcategory=14)
    toys=product.objects.filter(subcategory=13)
    categories=SubCategories.objects.filter(category=1)

    context={'logo':log,'user':user,'womens':womens,'mens':mens,
    'carousel':carousel,'cart':cart,'home':home,'shoe':shoe,'prodshirt':prodshirt,'watch':watch,'toys':toys,
    'categories':categories,'cat':request.POST.get("flexRadioDefault")}

    return render(request,'kids.html',context)


def appliance(request):
    log=templates.objects.get(pk=1)
    user=templates.objects.get(pk=2)
    womens=templates.objects.get(pk=3)
    mens=templates.objects.get(pk=4)
    carousel=templates.objects.get(pk=5)
    cart=templates.objects.get(pk=6)
    home=templates.objects.get(pk=7)
    pillow_cover=product.objects.filter(subcategory=19)
    bedsheets=product.objects.filter(subcategory=20)
    wallhanging=product.objects.filter(subcategory=21)
    cups=product.objects.filter(subcategory=22)
    showpiece=product.objects.filter(subcategory=23)
    categories=SubCategories.objects.filter(category=1)

    context={'logo':log,'user':user,'womens':womens,'mens':mens,
    'carousel':carousel,'cart':cart,'home':home,'pillow_cover':pillow_cover,'bedsheets':bedsheets,'wallhanging':wallhanging,'cups':cups,'showpiece':showpiece,
    'categories':categories,'cat':request.POST.get("flexRadioDefault")}

    return render(request,'appliance.html',context)



def beauty(request):
    log=templates.objects.get(pk=1)
    user=templates.objects.get(pk=2)
    womens=templates.objects.get(pk=3)
    mens=templates.objects.get(pk=4)
    carousel=templates.objects.get(pk=5)
    cart=templates.objects.get(pk=6)
    home=templates.objects.get(pk=7)
    lipstick=product.objects.filter(subcategory=15)
    kajal=product.objects.filter(subcategory=17)
    perfumes=product.objects.filter(subcategory=16)
    fhcare=product.objects.filter(subcategory=18)
    categories=SubCategories.objects.filter(category=1)

    context={'logo':log,'user':user,'womens':womens,'mens':mens,
    'carousel':carousel,'cart':cart,'home':home,'lipstick':lipstick,'kajal':kajal,'perfumes':perfumes,'fhcare':fhcare,
    'categories':categories,'cat':request.POST.get("flexRadioDefault")}

    return render(request,'beauty.html',context)


def cart(request):
    if request.method == "POST":
        global context
        log=templates.objects.get(pk=1)
        user=templates.objects.get(pk=2)
        cart=templates.objects.get(pk=6)
        dict=json.loads(request.POST.get('prodd'))
        ldict=list(map(int,dict.keys()))
        objects=product.objects.filter(pk__in=ldict)
        context={'logo':log,'user':user,'cart':cart,'object':objects,'dict':dict}
        
    return render(request,'cart.html',context)

def checkout(request):
    if request.method == "POST":
        global context
        dict=json.loads(request.POST.get('prodd'))
        ldict=list(map(int,dict.keys()))
        count=len(ldict)
        objects=product.objects.filter(pk__in=ldict)
        tcount=list(product.objects.filter(pk__in=ldict).values_list('dprice', flat=True)) # flat=True will remove the tuples and return the list  
        values=[]
        for i in tcount:
            val=int(i[3:])
            values.append(val)
        print(values)
        counts=[]
        for i in ldict:
            val=dict[str(i)]
            counts.append(val)
        print(counts)
        sum=0
        for i in range(len(ldict)):
            sum=sum+(values[i]*counts[i])
        print(sum)
        context={'object':objects,'dict':dict,'count':count,'sum':sum}
    return render(request,'checkout.html',context)
    

def productpage(request,id):
    log=templates.objects.get(pk=1)
    user=templates.objects.get(pk=2)
    cart=templates.objects.get(pk=6)
    if request.method == "GET":
        pi=product.objects.get(pk=id)
        prod=product.objects.filter(subcategory=pi.subcategory)
        tmp=list(prod)[:]
        random.shuffle(tmp)
    return render(request,"product.html",{"prod":pi,'logo':log,'user':user,'cart':cart,'prod1':tmp})

def payment(request):
    if request.method == "POST":
        fname=request.POST.get("firstname")
        state=request.POST.get("state")
        email=request.POST.get("email")
        city=request.POST.get("city")
        add=request.POST.get("address")
        zip=request.POST.get("zip")
        ord = order(fullname=fname,email=email,address=add,city=city,Zip=zip,state=state,order_date=datetime.today())
        ord.save()
        if order is not None:
            return redirect("/")
    return HTTPResponse(request,"the order had been placed successfully")
