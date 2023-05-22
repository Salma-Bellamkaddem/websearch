from django.urls import path 
from .import views

urlpatterns = [
    path('',views.projects,name="projects"),
    path('single-project/<str:pk>/',views.project,name="project"), 
    path('create-project/',views.createProject,name="create-project"),
    path('create-project/<str:pk>/',views.updateProject,name="update-project"),
    path('delete-project/<str:pk>/',views.deleteProject,name="delete-project"),

]