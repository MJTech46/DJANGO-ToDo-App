from django.shortcuts import render

# Create your views here.
def todolist(request):
    return render(request, 'Task/todolist.html')

def details(request):
    return render(request, 'Task/details.html')

def addtask(request):
    return render(request, 'Task/addtask.html')