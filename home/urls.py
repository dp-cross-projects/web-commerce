
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('/<str:user>', views.hello),
    # path('about/', views.about),
    # path('projects/', views.projects),
    # # path('task/<int:id>', views.tasks),
    # path('tasks/', views.tasks),
    # path('project/<int:id>', views.render_project),
    # path('newtask/', views.create_task)

]