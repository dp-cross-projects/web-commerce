
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout_page),
    path('<int:user_id>/<int:product_id>', views.add_product_to_cart),
    path('remove/<int:cart_id>', views.remove_product_from_cart)
]