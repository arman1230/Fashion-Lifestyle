from asyncio.windows_events import NULL
import http
from http.client import HTTPResponse
from math import prod
from pickle import GET
from unicodedata import category, name
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import SubCategories, categories, customer,product, Shubimage,templates
from datetime import datetime
import random
import json

# Create your views here.
#@login_required(login_url="/login")
def index(request):
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

def login(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pswd=request.POST.get("pswd")
        cust=customer.objects.get(username=uname)
        if cust.password == pswd:
            return redirect("/")
    return render(request,'login.html')
def signin(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        dob=request.POST.get("dob")
        gender=request.POST.get("gender")
        address=request.POST.get("tarea")
        pcode=request.POST.get("pcode")
        uname=request.POST.get("uname")
        pswd=request.POST.get("pswd")
        print(fname,lname,email,phone,dob,gender,address,pcode,uname,pswd)
        cust = customer(firstname=fname,lastname=lname,email=email,phone=phone,dob=dob,gender=gender,address=address,postal_code=pcode,username=uname,password=pswd,date_created=datetime.today())
        cust.save()
        return redirect("/")
            
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
