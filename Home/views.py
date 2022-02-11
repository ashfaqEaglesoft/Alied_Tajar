from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'Home/index.html')


def signin(request):
    if request.method=="POST":
        loginusername=request.POST['username']
        loginuserpassword=request.POST['password']
        user = authenticate(username=loginusername, password=loginuserpassword)
        if user is not None:
            login(request,user)
            messages.success(request,f"your are login in as {loginusername}")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentionls! Please Try again")
            return redirect("/")
    return render(request,'Home/signin.html')