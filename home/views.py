from django.http import HttpResponse, JsonResponse
from .models import Product
from django.shortcuts import get_object_or_404, render
from .forms import CreateTask

# Create your views here.
# def home(request):
#     return render(request, 'index.html')

# def hello(request, user):
#     return HttpResponse("<h1>Hello %s</h1>" % user)

# def about(request):
#     return HttpResponse("about")

# def projects(request):
#     projects = list(Project.objects.values())
#     return JsonResponse(projects, safe=False)

# def tasks(request):
#     # task = Task.objects.get(id=id)
#     # task = get_object_or_404(Task, id=id)
#     # return HttpResponse("Task: " % task.title)
#     tasks = list(Task.objects.all())
#     return render(request, 'tasks.html', {
#         'tasks': tasks
#     })

# def render_project(request, id):
#     title = Project.objects.get(id=id)
#     return render(request, 'project.html', {
#         'title': title.name
#     })

# def create_task(request):
#     return render(request, 'new_task.html', {
#         'form': CreateTask()
#     })



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