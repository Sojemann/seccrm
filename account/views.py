from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.forms import RegistrationForm, AccountForm
from django.contrib import messages
from .models import *

# Create your views here.


def registration_view(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()  
            username = form.cleaned_data.get('username')
            login(request,user)
            return redirect('login')
        else:
            form = RegistrationForm()
            return render(request,'account/register.html', {'form': form})

    return render(request,'account/register.html', {'form': form})

def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)
    

def logout_request(request):
    logout(request)

    messages.info(request, "Logged out successfully!")
    return redirect('login')


def userList(request):
    
    accounts = Account.objects.all()

    context = {
        'accounts': accounts
    }

    return render(request, 'account/user.html', context)

def userDetails(request, pk):

    account = Account.objects.get(id = pk)

    context = {
        'account': account
    }

    return render(request, 'account/userdetails.html', context)

def updateUser(request, pk):

    account = Account.objects.get(id=pk)

    form =AccountForm(instance = account)

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance = account)
        if form.is_valid():
            form.save()
            return redirect('user')

    context = {
        'form': form,
        'account': account
        }

    return render(request, 'account/updateuser.html', context)


def index(request):
    
    accounts = Account.objects.all()

    context = {
        'accounts': accounts
    }

    return render(request, 'account/index.html', context)


