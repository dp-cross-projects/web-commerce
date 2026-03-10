from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import UserHistory, UserOrder

# Backend User Profile Functions
# Get all user profiles?

# Get a user by id
# def get_userdata(request):
#     user_data = User.objects.get(username=request.user)
#     # print(user_data.username)
#     return user_data

# Create a user
# def create_or_update_user_data(request, id):
#     if(id):
#         print("Update user data")
#         return
#     else:
#         UserData.objects.create(
#             user_data = request.user_data,
#             name = request.name,
#             surname = request.surname,
#             address = request.address,
#             zip_code = request.zip_code,
#             province = request.province,
#             phone = request.phone
#         )
#         return

# Delete a user
# def delete_user(request, id):
#     UserData.objects.delete(UserData.objects.get(id=id))
#     return


# Backend User Order Functions
# Get user oder
def get_user_order(request):
    user_order = list(UserOrder.objects.all())
    return user_order

# Get user oder by id
def get_user_order_by_id(request):
    user_order = list(UserOrder.objects.get(id=id))
    return user_order



# Backend User History Functions
# Get all user_history profiles?
def get_user_history(request):
    user_history = list(UserHistory.objects.all())
    return user_history

# Get a user_history by id

# Create a user_history
def create_user_history(request):
    UserHistory.objects.create(
        user = request.user,
        date = request.date,
        product = request.product,
        category = request.category,
        brand = request.brand,
        model = request.model,
        total_payment = request.total_payment
    )
    return

# Update a user_history

# Delete a user_history




## Frontend functions
def user_page(request):
    return render(request, 'user/user_profile.html',{
        'userdata':request.user
    })