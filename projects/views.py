from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project, Tag
from .forms import projectForm
from django.db.models import Q
from .utils import  searchProjects
def projects(request):
    projects, search_query= searchProjects(request)

    context= {'projects':projects ,'search_query':search_query}
    return render(request,'projects/projects.html',context)

def project(request,pk): 
    projectObj = Project.objects.get(id=pk)
    context= {'project':projectObj}
    return render(request,'projects/single-project.html',context)

@login_required(login_url="login")
def createProject(request):
    profile =request.user.profile
    form =projectForm()

    if request.method=='POST':
         form =projectForm(request.POST,request.FILES)
         if form.is_valid():
             project= form.save(commit=False)
             project.owner = profile
             project.save()
             return redirect('projects')


    context={'form':form}
    return render(request,'projects/project-form.html',context)
# Create your views here.

@login_required(login_url="login")
def  updateProject(request,pk):
    context={}
    project=Project.objects.get(id=pk)
    form =projectForm(instance=project)
    template ='projects/project-form.html'

    if request.method =='POST':
        form=projectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context['form']=form
    return render(request,template,context)


@login_required(login_url="login")
def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method =='POST':
        project.delete()
        return redirect('projects')
    return render(request,'delete_template.html',{'object':project})
