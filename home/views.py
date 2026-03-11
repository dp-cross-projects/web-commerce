from django.http import HttpResponse, JsonResponse
from .models import Product
from django.shortcuts import render

## FRONTEND FUNCTIONS
# Render Home Page
def home_page(request):
    # Get product list
    products = list(Product.objects.all())

    # Get user logged data
    user = request.user

    # Render Home using user data and product list
    return render(request, 'index.html', {
        'user':user,
        'products':products
    })