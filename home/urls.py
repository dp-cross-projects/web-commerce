
from django.urls import path
from . import views

# Routes
urlpatterns = [
    # Home Page Route
    path('', views.home_page),
]