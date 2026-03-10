
from django.urls import path, include
from . import views, auth


urlpatterns = [
    path('',views.user_page),
    path('login/', auth.signin),
    path('logout', auth.signout),
    path('purchase',views.complete_purchase)
]