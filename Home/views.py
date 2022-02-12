from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm

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
            messages.warning(request,"Invalid Credentionls! Please Try again")
            return redirect("signin")
    return render(request,'Home/signin.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'Home/signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')
