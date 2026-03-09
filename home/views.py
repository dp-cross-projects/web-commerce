from django.http import HttpResponse, JsonResponse
from .models import Product
from django.shortcuts import get_object_or_404, render
from .forms import CreateTask

# Backend Products Functions
# Get all products
def get_product(request):
    product_list = list(Product.objects.all())
    return product_list

# Get a product by id
def get_product_by_id(request, id):
    product_item = list(Product.objects.get(id=id))
    return product_item

# Create a product
def create_product(request):
    Product.objects.create(
        name = request.name,
        category = request.category,
        brand = request.brand,
        model = request.model,
        description = request.description,
        price = request.price,
        tax = request.tax,
        discount = request.discount,
        quantity = request.quantity,
        image = request.image
    )
    return

# Update a product
# def update_product(request, id):
#     Product.objects.update()

# Delete a product
def delete_product(request,id):
    Product.objects.delete(Product.objects.get(id=id))
    return


## Frontend functions
# Create your views here.
def home_page(request):
    products = get_product(request)
    return render(request, 'index.html', {
        'products':products
    })

def about(request):
    return HttpResponse("about")