from django.http import HttpResponse
from django.shortcuts import render
from .models import CheckOut

# Backend CheckOut Functions
# Get all checkout?

# Get a checkout by id
def get_checkout(request, id):
    checkout_item = list(CheckOut.objects.get(id=id))
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
    return render(request, 'checkout/cart.html')