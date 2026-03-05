from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def hello(request, user):
    return HttpResponse("<h1>Hello %s</h1>" % user)

def about(request):
    return HttpResponse("about")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("Task: " % task.title)
    tasks = list(Task.objects.all())
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def render_project(request, id):
    title = Project.objects.get(id=id)
    return render(request, 'project.html', {
        'title': title.name
    })