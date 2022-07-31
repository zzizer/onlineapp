from django.shortcuts import render
from .models import Product

def shopping(request):
    
    products = Product.objects.all()
    
    return render(request, 'shopping.html', {'products':products})


def mycart(request):
    return render(request, 'mycart.html')