from django.http import HttpResponse
from django.shortcuts import render


# /products
def index(request):
    return HttpResponse("Hello World")


# /products/new
def new_product(request):
    return HttpResponse("New Product")
