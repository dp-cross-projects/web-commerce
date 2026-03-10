from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CheckOut
from .forms import PurchaseForm
from django.contrib.auth.models import User
from home.models import Product
# from .forms import CreateCheckout
# Backend CheckOut Functions
# Get all checkout?

# Get a checkout by user
def get_checkout(request):
    checkout_item = list(CheckOut.objects.filter(user=request.user))
    return checkout_item

# Create a checkout
# def create_checkout(request):
#     CheckOut.objects.create(
#         user = request.user,
#         product = request.product,
#         quantity = 1
#     )
#     return

# Update a checkout


# Delete a checkout
def delete_checkout(request, id):
    CheckOut.objects.delete(CheckOut.objects.get(id=id))
    return

## Frontend functions
def checkout_page(request):
    user = request.user
    cart = get_checkout(request)
    return render(request, 'checkout/cart.html',{
        'user':user,
        'cart':cart,
        'purchase_form':PurchaseForm
    })

def add_product_to_cart(request, user_id, product_id):
    # Get cart object
    user = User.objects.get(pk=user_id)
    product = Product.objects.get(pk=product_id)
    if(product.quantity >= 1):
        product.quantity -= 1
        product.save()

        item, cart_item = CheckOut.objects.get_or_create(
            user=user,
            product=product
        )
        item.quantity += 1
        item.save()
    return redirect('/')

def remove_product_from_cart(request, cart_id):
    # Get cart object
    cart_item = CheckOut.objects.get(pk=cart_id)

    product_set = Product.objects.filter(id=cart_item.product.id)
        
    if(cart_item.quantity <= 1):
        cart_item.delete()

    else:
        cart_item.quantity -= 1
        cart_item.save()

    for product in product_set:
                product.quantity += 1
                product.save()

    return redirect('/checkout')


