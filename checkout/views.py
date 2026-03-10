from django.http import HttpResponse
from django.shortcuts import render
from .models import CheckOut

# Backend CheckOut Functions
# Get all checkout?

# Get a checkout by user
def get_checkout(request):
    checkout_item = list(CheckOut.objects.filter(user=request.user))
    print(checkout_item)
    return checkout_item

# Create a checkout
def create_checkout(request):
    CheckOut.objects.create(
        user = request.user,
        product = request.product
    )
    return

# Update a checkout


# Delete a checkout
def delete_checkout(request, id):
    CheckOut.objects.delete(CheckOut.objects.get(id=id))
    return

## Frontend functions
def checkout_page(request):
    cart = get_checkout(request)
    return render(request, 'checkout/cart.html',{
        'cart':cart
    })