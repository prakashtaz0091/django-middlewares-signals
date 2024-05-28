from django.shortcuts import render
from django.http import HttpResponse
# from .signals import product_post_save, product_pre_save
# Create your views here.
from app.models import Product

def home(request):

    print("home view called")

    product = Product(name="Laptop")
    #pre_save signal
    product.save()
    #post_save signal

    return HttpResponse("This is view")



def secret_view(request):

    print("secret view called")

    return HttpResponse("This is top secret view")