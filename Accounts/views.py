from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout

# Create your views here.
def signin(request):
    if request.method == "GET":
        return render(request,"Accounts/signin.html")
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('todolist')
        else:
            message = "invalid credentials!"
            return render(request,"Accounts/signin.html", {"message":message})

def signup(request):
    if request.method == "GET":
        return render(request,"Accounts/signup.html")
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        conformpassword=request.POST.get("conformpassword")
        try:
            if password == conformpassword:
                user=User.objects.create_user(username=username,password=password)
                return redirect("signin")
            else:
                message="password doesnt match!"
                return render(request,"Accounts/signup.html", {"message":message})
        except Exception as e:
            return render(request,"Accounts/signup.html",{"message":e})
            
def signout(request):
    auth_logout(request)
    return redirect("signin")

def resetpass(request):
    return render(request,"Accounts/resetpass.html")


def home(request):
    return render(request,"Accounts/home.html")