from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


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
            return redirect('home')
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
                message="Password doesnt match!"
                return render(request,"Accounts/signup.html", {"message":message})
        except Exception as e:
            return render(request,"Accounts/signup.html",{"message":e})


@login_required(login_url='signin')       
def signout(request):
    auth_logout(request)
    return redirect("signin")


@login_required(login_url='signin')
def resetpass(request):
    if request.method == "GET":
        return render(request,"Accounts/resetpass.html",{"username":request.user})
    if request.method == "POST":
        username=request.user
        password=request.POST.get("password")
        conformpassword=request.POST.get("conformpassword")
        if password == conformpassword:
            user=User.objects.get(username=username)
            user.password=make_password(password)
            user.save()
            auth_logout(request)
            return redirect("signin")
        else:
            message="Password doesnt match!"
            return render(request,"Accounts/resetpass.html",{"username":request.user,"message":message})


@login_required(login_url='signin')
def manage(request):
    return render(request, 'Accounts/manage.html',{"request":request})


@login_required(login_url='signin')
def remove_acc(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user)
        user.delete()
        return redirect('signin')