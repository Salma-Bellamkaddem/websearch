from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import projectForm



def projects(request): 
    projects = Project.objects.all()
    context= {'projects':projects}
    return render(request,'projects/projects.html',context)

def project(request,pk): 
    projectObj = Project.objects.get(id=pk)
    context= {'project':projectObj}
    return render(request,'projects/single-project.html',context)

def createProject(request):
    form =projectForm()

    if request.method=='POST':
         form =projectForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('projects')


    context={'form':form}
    return render(request,'projects/project-form.html',context)
# Create your views here.
def  updateProject(request,pk):
    context={}
    project=Project.objects.get(id=pk)
    form =projectForm(instance=project)
    template ='projects/project-form.html'

    if request.method =='POST':
        form=projectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context['form']=form
    return render(request,template,context)

def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method =='POST':
        project.delete()
        return redirect('projects')
    return render(request,'projects/delete.html',{'object':project})
