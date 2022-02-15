from http.client import HTTPS_PORT
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm,BusinessForm

from .models import Business

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

# Add products 
def add_business(request):
    form = BusinessForm(request.POST or None, request.FILES or None)
    if request.method=="POST":
        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()
            messages.add_message(request, messages.INFO, 'Products Add in Inventory')
        else:
            messages.add_message(request, messages.WARNING, 'Oops! Products did not Add in Inventory')
    context={
        "p_form":form,
    }
    return render(request,"home/add_business.html",context)

def show_business(request):
    form=Business.objects.all()
    context={
        'form':form
    }
    return render(request,'Home/showbusiness.html',context)

def update_business(request,id):
    b_data=Business.objects.filter(id=id)
    context={
        'b_data':b_data,
    }
    return render(request,"Home/updatebusiness.html",context)


