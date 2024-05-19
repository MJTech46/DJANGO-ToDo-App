from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request,"Accounts/signin.html")

def signup(request):
    return render(request,"Accounts/signup.html")

def resetpass(request):
    return render(request,"Accounts/resetpass.html")