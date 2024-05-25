from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context={
            "user":None
        }
    if request.user.is_authenticated:
        context["user"]=request.user
        
    return render(request,"Task/home.html", context)


@login_required(login_url='signin')
def todolist(request):
    context = {
            "tasklist": Task.objects.filter(user=request.user)
        }
    
    if request.method == 'GET':
        return render(request, 'Task/todolist.html', context)
    
    if request.method == 'POST':
        pk=request.POST.get('pk')
        action=request.POST.get('action')
        postobj=Task.objects.get(pk=pk)
        if action == "delete":
            postobj.delete()
        elif action == "done":
            postobj.status=Task.DONE
            postobj.save()
        elif action == "not done":
             postobj.status=Task.PENDING
             postobj.save()
        return redirect('todolist')


@login_required(login_url='signin')
def details(request):
    if request.method == "POST" and request.POST.get('from') == "todolist": #todolist site post req
        context = {
            "tasks": Task.objects.filter(pk=request.POST.get('pk'))
        }
        return render(request, 'Task/details.html', context)
    

    if request.method == "POST" and request.POST.get('from') == "details": #details page post req
        pk=request.POST.get('pk')
        action=request.POST.get('action')
        postobj=Task.objects.get(pk=pk)
        if action == "delete":
            postobj.delete()
        elif action == "submit":
            postobj.name=request.POST.get('name')
            postobj.description=request.POST.get('description')
            if request.POST.get('checkbox'):
                postobj.status=Task.DONE
            else:
                postobj.status=Task.PENDING
            postobj.save()
        return redirect("todolist")



@login_required(login_url='signin')
def addtask(request):
    if request.method == 'GET':
        return render(request, 'Task/addtask.html')
    if request.method == 'POST':
        post_obj=Task(
            name=request.POST.get('taskname'),
            description=request.POST.get('description'),
            user=request.user
        )
        post_obj.save()
        return redirect('todolist')