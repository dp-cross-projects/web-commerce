from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CheckOut
from .forms import PurchaseForm
from django.contrib.auth.models import User
from home.models import Product

## FRONTEND FUNCTIONS

## Renders CheckOut (cart)
def checkout_page(request):
    # Get User logged
    user = request.user

    # Get cart items from user
    cart = list(CheckOut.objects.filter(user=request.user))

    # Init cart cost 
    total_amount = 0

    # Iterate cart items and calculate the total cost from the cart
    for item in cart:
        # Price
        price = (item.product.price * item.quantity)
        # Discount
        discount = 1 - item.product.discount
        # Tax
        tax = 1 + item.product.tax

        # Add item cost to cart
        total_amount += (price * discount * tax)

    # Render cart template using user data, cart data, cart cost and purchase form (import)
    return render(request, 'checkout/cart.html',{
        'user':user,
        'cart':cart,
        'total_amount': total_amount,
        'purchase_form':PurchaseForm
    })

## Add a product to cart
def add_product_to_cart(request, user_id, product_id):
    # Get user data
    user = User.objects.get(pk=user_id)

    # Get product data
    product = Product.objects.get(pk=product_id)

    # Filter where product is available
    if(product.quantity >= 1):
        # Remove 1 from product quantity
        product.quantity -= 1
        product.save()

        # Get or Create the item on cart
        item, cart_item = CheckOut.objects.get_or_create(
            user=user,
            product=product
        )

        # Adds 1 to cart product quantity
        item.quantity += 1
        item.save()
    
    # Always return to Home
    return redirect('/')

## Removes an item from cart
def remove_product_from_cart(request, cart_id):
    # Get cart item
    cart_item = CheckOut.objects.get(pk=cart_id)

    # Get product related
    product_set = Product.objects.filter(id=cart_item.product.id)

    # If we substract the last item, remove the cart item    
    if(cart_item.quantity <= 1):
        cart_item.delete()

    # If there are more than 1 item, then substract 1
    else:
        cart_item.quantity -= 1
        cart_item.save()

    # Adds 1 to product quantity (recover item)
    for product in product_set:
                product.quantity += 1
                product.save()

    # Always return to /checkout
    return redirect('/checkout')


