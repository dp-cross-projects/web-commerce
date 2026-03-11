
from django.urls import path, include
from . import views, auth

## User Routes
urlpatterns = [
    # User Main Page - Method Supported: GET
    path('',views.user_page),

    # Register Route - Method Supported: GET, POST
    path('register/', auth.signup),

    # Login Route - Method Supported: GET, POST
    path('login/', auth.signin),

    # Logout Route - Method Supported: GET
    path('logout', auth.signout),

    # Purchase Route - Method Supported: POST
    path('purchase',views.complete_purchase)
]