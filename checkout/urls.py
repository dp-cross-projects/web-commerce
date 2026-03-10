
from django.urls import path
from . import views

## CheckOut Routes
urlpatterns = [
    # Cart Main Page - Method Supported: GET
    path('', views.checkout_page), 

    # Add item to cart /{user_id}/{product_id} - Method Supported: POST
    path('<int:user_id>/<int:product_id>', views.add_product_to_cart), 

    # Remove item from cart /{cart_id} - Method Supported: POST
    path('remove/<int:cart_id>', views.remove_product_from_cart) 
]