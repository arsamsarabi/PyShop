from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /products
def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


# /products/new
def new_product(request):
    return HttpResponse("New Product")
