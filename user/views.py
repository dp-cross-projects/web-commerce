from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserHistory, UserOrder
from checkout.models import CheckOut
# from django.forms import ModelForm
from .forms import UserDataForm
## FRONTEND FUNCTIONS

# Render User Profile
def user_page(request):

    # Get User logged
    user = request.user

    # Get User Orders
    user_order = UserOrder.objects.filter(user=request.user)

    # Init User purchased items from User History
    user_history = []

    # Iterate and set User purchased items from User History
    for item in user_order:
        # Filter items from User Order
        user_history.append(UserHistory.objects.filter(user_order=item))        
    
    # Render User Profile using user data, user orders and
    # user history filtered by user order, and user data form
    return render(request, 'user/user_profile.html',{
        'user': user,
        'user_order': user_order,
        'user_history': user_history,
        'user_data_form': UserDataForm
    })

# Complete purchase and move from cart to User Order & User History
def complete_purchase(request):
    # Get cart from user
    cart = CheckOut.objects.filter(user=request.user)

    # Init total amount for operation
    total_amount = 0

    # Set total amount from items in cart
    for item in cart:
        # Price
        price = (item.product.price * item.quantity)
        # Discount
        discount = 1 - item.product.discount
        # Tax
        tax = 1 + item.product.tax

        # Calculate price by item using Price, Discount and Tax
        total_amount += (price * discount * tax)

    # Create User Order from /checkout form POST action,
    # user data and total amount calculated
    user_order = UserOrder.objects.create(
        user = request.user,
        address = request.POST['address'],
        zip_code = request.POST['zip_code'],
        province = request.POST['province'],
        phone = request.POST['phone'],
        total_amount = total_amount
    )

    # Copy items from cart to User History
    for item in cart:
        UserHistory.objects.create(
            user_order=user_order,
            product=item.product,
            category=item.product.category,
            brand=item.product.brand,
            model=item.product.model
        )

    # Clean the user cart
    cart.delete()

    # Redirect to User Profile
    return redirect('/user')
     