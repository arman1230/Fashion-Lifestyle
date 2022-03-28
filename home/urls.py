from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.user_login,name="login"),
    path('signin',views.signin,name="signin"),
    path('mens',views.mens,name="mens"),
    path('womens',views.womens,name="womens"),
    path('kids',views.kids,name="kids"),
    path('appliance',views.appliance,name="appliance"),
    path('beauty',views.beauty,name="beauty"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('logout',views.user_logout,name="logout"),
    path('payment',views.payment,name="payment"),
    path('product/<int:id>/',views.productpage,name="productdata")
]